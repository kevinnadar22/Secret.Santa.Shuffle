import logging
from secret_santa_app import create_app, socketio

app = create_app()

if __name__ == "__main__":
    logging.info("Starting server")
    socketio.run(app)
    