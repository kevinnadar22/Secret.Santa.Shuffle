from flask import Flask

from .room import socketio
from .route import bp


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(bp)

    socketio.init_app(app)

    return app
