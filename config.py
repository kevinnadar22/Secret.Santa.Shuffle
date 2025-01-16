import os
import logging


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    LOG_LEVEL = logging.INFO


class Cache(object):
    ROOM_CACHE = {}
