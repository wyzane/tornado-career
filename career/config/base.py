import os
import time


BASE_DIR = os.path.dirname(__file__)

# Server Config
options = {
    "port": 8002,
}

# settings
settings = {
    "debug": True,
    "secret_key": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
}

# Pagination
PAGE = 1
PAGE_SIZE = 10

# Url
NONE_TOKEN_URLS = [
    "/api/v1/user/register",
    "/api/v1/user/login",
]

# JWT Config
JWT_AUTH = {
    "EXPIRE": int(time.time()) + 3600,
}
