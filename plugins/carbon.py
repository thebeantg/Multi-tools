from pyrogram import filters, Client as bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
from aiohttp import ClientSession

import aiofiles
import speedtest
from PIL import Image
from pyrogram.types import Message

aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


C = "**MADE WITH ❤️ BY >JEOL**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/beta_boTZ")
]]
)


@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "REPLY TO A TEXT MESSAGE TO MAKE CARBON."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "REPLY TO A TEXT MESSAGE TO MAKE CARBON."
        )
    user_id = message.from_user.id
    m = await message.reply_text("Processing...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading..")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
