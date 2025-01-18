import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    LOG_LEVEL = logging.INFO
    
    # Domain configuration
    DOMAIN = os.environ.get("DOMAIN", "http://localhost:5000")
    
    # Compression settings
    COMPRESS_MIMETYPES = [
        'text/html',
        'text/css',
        'text/xml',
        'application/json',
        'application/javascript',
        'text/javascript',
        'text/plain'
    ]
    COMPRESS_LEVEL = 6  # Higher level = better compression but more CPU
    COMPRESS_MIN_SIZE = 500  # Minimum size in bytes to compress
    COMPRESS_ALGORITHM = ['gzip', 'br']  # Support both gzip and brotli
    COMPRESS_BR_LEVEL = 4  # Brotli compression level
    COMPRESS_BR_MODE = 0  # Generic mode for brotli
    
    # Cache settings
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year in seconds
    
    @property
    def CLEAN_DOMAIN(self):
        return self.DOMAIN.replace("http://", "").replace("https://", "")


class Cache(object):
    ROOM_CACHE = {}
