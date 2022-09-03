import os
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from helper.fsub import ForceSub
from MULTIBOT import Client

__MODULE__ = "Telegraph"
__HELP__ = """
Send me any image or video under 5mb"""

@Client.on_message(filters.media & filters.private)
async def telegraph_upload(bot, update):
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return 
    text = await update.reply_text(
        text="<code>Downloading to My Server ...</code>",
        disable_web_page_preview=True
    )
    media = await update.download()
    
    await text.edit_text(
        text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>",
        disable_web_page_preview=True
    )
    
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(
            text=f"Error :- {error}",
            disable_web_page_preview=True
        )
        return
    
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return
    
    await text.edit_text(
        text=f"<b>Link :-</b> <code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{response[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
            ]]
        )
    )






