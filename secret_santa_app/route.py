from flask import Blueprint, render_template, current_app, request, redirect, url_for
from .utils import room_id_generator
from .models import Room, User
from config import Cache
from flask_socketio import SocketIO

bp = Blueprint("main", __name__)

# Update SocketIO initialization
socketio = SocketIO(
    cors_allowed_origins="*",
    ping_timeout=60,
    ping_interval=25,
    reconnection=True,
    reconnection_attempts=5,
    reconnection_delay=1000,
    reconnection_delay_max=5000
)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/create-room", methods=["POST"])
def create_room():
    data = request.form
    name = data.get("name")
    room_code = room_id_generator()
    room = Room(id=room_code, users=[], admin=User.get_dummy_user())
    Cache.ROOM_CACHE[room_code] = room
    return redirect(url_for("main.room", room_code=room_code, name=name))


@bp.route("/join-room", methods=["POST"])
def join_room():
    data = request.form
    name = data.get("name")
    room_code = data.get("room_code")
    # if room code is not in cache, redirect to index with an error message
    if room_code not in Cache.ROOM_CACHE:
        context = {"error": "Room not found"}
        return render_template("index.html", **context)
    # if room code is in cache and same name user already exists, return error message
    if name in [user.name for user in Cache.ROOM_CACHE[room_code].users]:
        context = {"error": "Name already exists in this room, try a different name"}
        return render_template("index.html", **context)
    return redirect(url_for("main.room", room_code=room_code, name=name))


@bp.route("/room/<room_code>")
def room(room_code):
    name = request.args.get("name")
    return render_template("room.html", room_code=room_code, name=name)
