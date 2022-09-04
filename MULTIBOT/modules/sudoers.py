
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters
from pyrogram.errors import FloodWait

from MULTIBOT import (
    BOT_ID,
    ADMIN as SUDOERS,
    Client as app,
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

__MODULE__ = "Sudoers"
__HELP__ = """
/stats - To Check System Status.

/broadcast - To Broadcast A Message To All Groups.
"""


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


# Gban





# Broadcast


@app.on_message(filters.command("broadcast") & SUDOERS & ~filters.edited)
@capture_err
async def broadcast_message(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage**:\n/broadcast [MESSAGE]")
    sleep_time = 0.1
    text = message.text.split(None, 1)[1]
    sent = 0
    schats = await get_served_chats()
    chats = [int(chat["chat_id"]) for chat in schats]
    m = await message.reply_text(
        f"Broadcast in progress, will take {len(chats) * sleep_time} seconds."
    )
    for i in chats:
        try:
            await app.send_message(i, text=text)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"**Broadcasted Message In {sent} Chats.**")


