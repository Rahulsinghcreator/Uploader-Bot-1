import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID", "27258871"))
    API_HASH = os.environ.get("API_HASH")
