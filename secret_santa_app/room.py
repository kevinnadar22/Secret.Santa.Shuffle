import random
from flask import request
from .extensions import socketio
from flask_socketio import emit, join_room, close_room
from config import Cache
from .models import User

# Add connection tracking
CONNECTED_USERS = {}

@socketio.on("connect")
def handle_connect():
    CONNECTED_USERS[request.sid] = {"connected": True, "room": None}
    emit("connection_response", {"status": "connected"})

@socketio.on("disconnect")
def handle_disconnect():
    user_sid = request.sid
    if user_sid in CONNECTED_USERS:
        room_id = CONNECTED_USERS[user_sid].get("room")
        if room_id:
            handle_user_disconnect(user_sid, room_id)
        del CONNECTED_USERS[user_sid]

def handle_user_disconnect(user_sid, room_id):
    room = Cache.ROOM_CACHE.get(room_id)
    if not room:
        return

    # Remove disconnected user
    room.users = [user for user in room.users if user.id != user_sid]

    # Handle admin reassignment if needed
    if room.admin.id == user_sid and room.users:
        room.admin = room.users[0]

    # Delete empty rooms and cleanup
    if not room.users:
        del Cache.ROOM_CACHE[room_id]
        close_room(room_id)
    else:
        Cache.ROOM_CACHE[room_id] = room
        emit("room_joined", room.dict(), to=room_id)

@socketio.on("join_room")
def handle_join_room(data):
    try:
        # Input validation
        if not data.get("name") or not data.get("roomCode"):
            emit("error", {"message": "Invalid room data"})
            return

        room_code = data["roomCode"]
        user = User(id=request.sid, name=data["name"])

        # Room existence check
        room = Cache.ROOM_CACHE.get(room_code)
        if not room:
            emit("room_not_found", {
                "status": "room_not_found", 
                "message": "Room not found"
            })
            return

        # Check if user is already in the room
        if request.sid in [u.id for u in room.users]:
            # Only emit room state if user is actually in this room
            if room_code == CONNECTED_USERS[request.sid].get("room"):
                emit("room_joined", room.dict(), to=room_code)
            return

        # Name duplicate check
        if user.name in [u.name for u in room.users]:
            emit("name_error", {
                "status": "error",
                "message": "Name already exists in this room, try a different name"
            })
            return

        # Handle first user case
        if len(room.users) == 0 and room.admin.id == "":
            room.users = []
            room.admin = user

        # Join room and update state
        room.users.append(user)
        Cache.ROOM_CACHE[room_code] = room
        join_room(room_code)
        CONNECTED_USERS[request.sid]["room"] = room_code
        
        # Notify room
        emit("room_joined", room.dict(), to=room_code)

    except Exception as e:
        emit("error", {
            "message": "Failed to join room. Please try again."
        })
        print(f"Error in handle_join_room: {str(e)}")

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

@socketio.on("kick_user")
def handle_kick_user(data):
    room_code = data.get("roomCode")
    user_id_to_kick = data.get("userId")

    room = Cache.ROOM_CACHE.get(room_code)
    if not room:
        emit("error", {"message": "Room not found"})
        return

    # Find and remove the kicked user
    kicked_user = None
    for user in room.users[:]:  # Create a copy to iterate
        if user.id == user_id_to_kick:
            kicked_user = user
            room.users.remove(user)
            break

    if kicked_user:
        # Emit to all users in the room
        emit(
            "user_kicked",
            {
                "kickedUserId": kicked_user.id,
                "users": [user.to_dict() for user in room.users],
                "admin": room.admin.to_dict(),
            },
            to=room_code,
        )
