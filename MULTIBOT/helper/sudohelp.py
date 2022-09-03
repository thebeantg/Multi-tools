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


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("dyno", CMD))         
async def bot_status(client,message):
    if HEROKU_API_KEY:
        try:
            server = heroku3.from_key(HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

                quota_details = f"""
💫SERVER STATUS💫
💠 ToTal dyno ➪ {total}hr 𝖿𝗋𝖾𝖾 𝖽𝗒𝗇𝗈!
 
💠 Dyno used ➪ {used} 𝖧𝗈𝗎𝗋𝗌 ( {usedperc}% )
        
💠 Dyno remaining ➪ {hours} 𝖧𝗈𝗎𝗋𝗌 ( {leftperc}% )
        
💠 Approximate days ➪ {days} days left!"""

            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**Disk Details**\n\n" \
            f"> USED  :  {used} / {total}\n" \
            f"> FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝘁𝗮𝘁𝘂𝘀 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗕𝗼𝘁\n\n"
        "DB Status\n"
        f"➪ 𝖡𝗈𝗍 𝖴𝗉𝗍𝗂𝗆𝖾: {uptime}\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="md"
    )

 
@Client.on_message(filters.command("users") & filters.user(ADMIN))
async def get_stats(bot :Client, message: Message):
    mr = await message.reply('**𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝙳𝙴𝚃𝙰𝙸𝙻𝚂.....**')
    total_users = await db.total_users_count()
    await mr.edit( text=f"🔍 TOTAL USER'S = `{total_users}`")

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("broadcast started !") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await db.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await db.delete_user(user['id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"Broadcast in progress:\nnTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"Broadcast Completed:\nCompleted in `{completed_in}`.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")
 
         
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : deactivated")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : blocked the bot")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : user id invalid")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500

