import os
import re
import logging
import logging.config
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from variables import FORCE_SUB

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class App(Client):

    def __init__(self):
        super().__init__(
            "multibot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

print="BOT STARTED"
bot = App()
bot.run()
