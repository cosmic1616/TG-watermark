import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = os.getenv("API_ID","23630387")
    API_HASH = os.getenv("API_HASH","3139998ebc89c2bc1873b794689f8e56")
    LOG_CHANNEL = os.getenv("LOG_CHANNEL","-1002396213226")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL","-1002396213226")
    OWNER_ID = int(os.getenv("OWNER_ID","7590766084"))
    DOWN_PATH = "downloads"
    PRESET = "ultrafast"
