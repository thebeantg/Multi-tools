
import asyncio
import time
from inspect import getfullargspec
from os import path
from variables import DB_URL as MONGO_URL
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen
from Python_ARQ import ARQ
from telegraph import Telegraph

is_config = path.exists("variables.py")

if is_config:
    from variables import *
else:
    from sample_config import *


LOG_GROUP_ID = LOG_CHANNEL
GBAN_LOG_GROUP_ID = LOG_CHANNEL
MESSAGE_DUMP_CHAT = LOG_CHANNEL
MOD_LOAD = []
MOD_NOLOAD = []
SUDOERS = ADMIN
bot_start_time = time.time()



mongo_client = MongoClient(MONGO_URL)
db = mongo_client.multibot

class Log:
    def __init__(self, save_to_file=False, file_name="multi.log"):
        self.save_to_file = save_to_file
        self.file_name = file_name

    def info(self, msg):
        print(f"[+]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[INFO]({time.ctime(time.time())}): {msg}\n")

    def error(self, msg):
        print(f"[-]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[ERROR]({time.ctime(time.time())}): {msg}\n")











aiohttpsession = ClientSession()



Client = Client("multibot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

Client.start()

x = Client.get_me()

BOT_ID = x.id
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id





telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
