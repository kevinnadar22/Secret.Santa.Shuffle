from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    jsonify,
)
from .utils import room_id_generator
from .models import Room, User
from config import Cache


bp = Blueprint("main", __name__)


# Add cache headers
@bp.after_request
def add_header(response):
    if "Cache-Control" not in response.headers:
        # Cache static files for longer
        if request.path.startswith("/static/"):
            response.cache_control.public = True
            response.cache_control.max_age = 300  # 5 minutes default cache
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


# update wishlist
@bp.route("/update-wishlist", methods=["POST"])
def update_wishlist():
    """Update a specific user's wishlist in a Secret Santa room
    
    Expected POST data:
        - wishlist: str - The new wishlist content
        - room_code: str - The room identifier 
        - user_id: str - The ID of the user whose wishlist to update
        
    Returns:
        JSON response indicating success or error
    """
    try:
        # Get and validate required data
        data = request.form
        wishlist = data.get("wishlist", "").strip()
        room_code = data.get("room_code", "").strip()
        user_id = data.get("user_id", "").strip()

        if not all([wishlist, room_code, user_id]):
            return jsonify({
                "status": "error", 
                "message": "Missing required fields"
            }), 400

        # Get room from cache
        room = Cache.ROOM_CACHE.get(room_code)
        if not room:
            return jsonify({
                "status": "error", 
                "message": "Room not found"
            }), 404

        # Find and update specific user's wishlist
        user = next((user for user in room.users if user.id == user_id), None)
        if not user:
            return jsonify({
                "status": "error", 
                "message": "User not found in room"
            }), 404

        # Update wishlist and save back to cache
        user.wishlist = wishlist
        Cache.ROOM_CACHE[room_code] = room

        return jsonify({
            "status": "success",
            "message": "Wishlist updated successfully",
            "data": {
                "user_id": user_id,
                "wishlist": wishlist
            }
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": f"An error occurred: {str(e)}"
        }), 500


@bp.route("/sitemap.xml")
def sitemap():
    """Generate sitemap.xml"""
    return render_template("sitemap.xml"), 200, {"Content-Type": "application/xml"}


@bp.route("/robots.txt")
def robots():
    """Serve robots.txt"""
    return render_template("robots.txt"), 200, {"Content-Type": "text/plain"}
