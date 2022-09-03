
import asyncio
import os
import subprocess
import time
import os
import math
import time
import heroku3
import requests
from variables import ADMIN, HEROKU_API_KEY
from pyrogram import filters

CMD = ['.', '/']

BOT_START_TIME = time.time()

import psutil
from pyrogram import filters
from pyrogram.errors import FloodWait

from MULTIBOT import (
    BOT_ID,
    GBAN_LOG_GROUP_ID,
    SUDOERS,
    bot_start_time,
)
from helper.errors import capture_err
from plugins.utils import formatter
from MULTIBOT import Client
from plugins.utils.dbfunctions import (
    add_gban_user,
    get_served_chats,
    is_gbanned_user,
    remove_gban_user,
)
from plugins.utils.functions import extract_user, extract_user_and_reason, restart
import time
import asyncio 
import logging 
import datetime
from variables import ADMIN
from helper.database import db
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



__MODULE__ = "Sudoers"
__HELP__ = """
/broadcast - To Broadcast A Message To All Groups.

/dyno - to check heroku dyno
"""


# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
MULTI BOT
------------------
UPTIME: {formatter.get_readable_time(bot_uptime)}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
"""
    return stats




