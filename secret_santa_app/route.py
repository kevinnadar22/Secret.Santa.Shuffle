from flask import Blueprint, render_template, request, redirect, url_for, make_response
from .utils import room_id_generator
from .models import Room, User
from config import Cache


bp = Blueprint("main", __name__)


# Add cache headers
@bp.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.cache_control.public = True
        response.cache_control.max_age = 300  # 5 minutes default cache

        # Cache static files for longer
        if request.path.startswith('/static/'):
            response.cache_control.max_age = 31536000  # 1 year

    return response


@bp.route("/")
def index():
    """Home page"""
    response = make_response(render_template("index.html"))
    response.headers["Vary"] = "Accept-Encoding"
    return response


@bp.route("/create-room", methods=["POST"])
def create_room():
    """Create a new room"""
    data = request.form
    name = data.get("name")
    room_code = room_id_generator()
    room = Room(id=room_code, users=[], admin=User.get_dummy_user())
    Cache.ROOM_CACHE[room_code] = room
    return redirect(url_for("main.room", room_code=room_code, name=name))


@bp.route("/join-room", methods=["POST"])
def join_room():
    """Join an existing room"""
    data = request.form
    name = data.get("name")
    room_code = data.get("room_code")
    return redirect(url_for("main.room", room_code=room_code, name=name))


@bp.route("/room/<room_code>")
def room(room_code):
    """Room page"""
    name = request.args.get("name") or ""
    response = make_response(
        render_template("room.html", room_code=room_code, name=name)
    )
    response.headers["Vary"] = "Accept-Encoding"
    return response


@bp.route("/sitemap.xml")
def sitemap():
    """Generate sitemap.xml"""
    return render_template("sitemap.xml"), 200, {"Content-Type": "application/xml"}


@bp.route("/robots.txt")
def robots():
    """Serve robots.txt"""
    return render_template("robots.txt"), 200, {"Content-Type": "text/plain"}
