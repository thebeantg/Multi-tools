
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters
from pyrogram.errors import FloodWait

from MULTIBOT import (
    BOT_ID,
    ADMIN,
    Client,
    bot_start_time,
)
from helper.errors import capture_err
from plugins.utils import formatter
from plugins.utils.dbfunctions import (
    add_gban_user,
    get_served_chats,
    is_gbanned_user,
    remove_gban_user,
)
from plugins.utils.functions import extract_user, extract_user_and_reason, restart
import asyncio
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant
from helper.database import insert, getid

__MODULE__ = "Sudoers"
__HELP__ = """
/stats - To Check System Status.

/broadcast - To Broadcast A Message To All Groups.
"""

WAIT_MSG = """"<b>Processing ...</b>"""

# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
------------------
UPTIME: {formatter.get_readable_time(bot_uptime)}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
"""
    return stats




