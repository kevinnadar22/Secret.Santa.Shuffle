from flask import Flask
from config import Config
from flask_sitemap import Sitemap
from .room import socketio
from .route import bp
from flask_compress import Compress


compress = Compress()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Sitemap configuration
    app.config["SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS"] = True
    app.config["SITEMAP_URL_SCHEME"] = (
        "https" if "https://" in Config.DOMAIN else "http"
    )

    # Initialize compression before other extensions
    compress.init_app(app)
    
    # Initialize other extensions
    ext = Sitemap(app=app)
    app.register_blueprint(bp)
    socketio.init_app(app)

    return app
