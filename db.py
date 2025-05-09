import os
from tortoise import Tortoise

# from dotenv import load_dotenv
#
# load_dotenv()
#
# BOT_TOKEN = os.getenv('BOT_TOKEN')
# BOT_USERNAME = os.getenv('BOT_USERNAME')
# DB_NAME = os.getenv('DB_NAME')
# DB_USER = os.getenv('DB_USER')
# DB_PASS = os.getenv('DB_PASS')
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')

# postgres://postgres:qwerty123@localhost:5432/events
# DB_URL = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

DATABASE_URL = "sqlite://db.sqlite3"

DB_CONFIG = {
    "connections": {
        "default": f"{DATABASE_URL}",
    },
    "apps": {
        "models": {
            "models": ["models.user", "aerich.models"],
            "default_connection": "default",
        }
    }
}


async def init_db():
    await Tortoise.init(config=DB_CONFIG)
