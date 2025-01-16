import random
from flask import request
from .extensions import socketio
from flask_socketio import emit, join_room
from config import Cache
from .models import User


# connect to the socket
@socketio.on("connect")
def handle_connect():
    print(f"Client connected with sid: {request.sid}")
    emit("connection_response", {"status": "connected"})


@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected with sid: {request.sid}")
    for room_id, room in Cache.ROOM_CACHE.items():
        # Check if user is in this room
        user_ids = [user.id for user in room.users]
        if request.sid in user_ids:
            # Remove disconnected user
            room.users = [user for user in room.users if user.id != request.sid]
            
            # Handle admin reassignment if needed
            if room.admin.id == request.sid and room.users:
                room.admin = room.users[0]
            
            # Delete empty rooms
            if not room.users:
                del Cache.ROOM_CACHE[room_id]
            else:
                Cache.ROOM_CACHE[room_id] = room
                # Emit updated room state to remaining users
                emit("room_joined", room.dict(), to=room_id)
            break


@socketio.on("join_room")
def handle_join_room(data):
    print(f"Joining room with data: {data}")
    room_code = data["roomCode"]
    if not room_code:
        return
    user = User(id=request.sid, name=data["name"])

    if room_code not in Cache.ROOM_CACHE:
        return emit("room_not_found", {"status": "room_not_found", "message": "Room not found"})
    
    room = Cache.ROOM_CACHE[room_code]

    # Check if user already exists in room,
    if user.id in [user.id for user in room.users]:
        emit("room_joined", room.dict(), to=room_code)
        return
    
    # check if user exists by same name, return error message
    if user.name in [user.name for user in room.users]:
        return emit("error", {"status": "error", "message": "Name already exists in this room, try a different name"})

    # If only one user with empty id exists, remove them and set new user as admin
    if len(room.users) == 0 and room.admin.id == "":
        room.users = []
        room.admin = user

    room.users.append(user)
    Cache.ROOM_CACHE[room_code] = room
    join_room(room_code)
    # print(room.dict(), file=open("room.json", "w"))
    emit("room_joined", room.dict(), to=room_code)


@socketio.on("leave_room")
def handle_leave_room(data):
    print(f"Leaving room with data: {data}")


@socketio.on("start_raffle")
def handle_start_raffle(data):
    print(f"Starting raffle with data: {data}")
    room = Cache.ROOM_CACHE[data["roomCode"]]
    # get users in room
    users = room.users
    # shuffle users
    random.shuffle(users)
    # assign secret santa to each user
    for i, user in enumerate(users):
        user.secret_santa = users[(i + 1) % len(users)]
    Cache.ROOM_CACHE[data["roomCode"]] = room

    emit("raffle_started", room.dict(), to=data["roomCode"])