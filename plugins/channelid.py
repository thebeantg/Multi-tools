from pyrogram import filters
from pyrogram import Client
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.fsub import ForceSub


@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    FSub = await ForceSub(motech, msg)
    if FSub == 400:
        return
    if msg.forward_from:
        text = "<u>๐๐ข๐ฅ๐ช๐๐ฅ๐ ๐จ๐ฆ๐๐ฅ๐ก๐๐ ๐</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>๐๐ข๐ง ๐๐ก๐๐ข</u>"
        else:
            text += "<u>๐จ๐ฆ๐๐ฅ ๐๐ก๐๐ข</u>"
        text += f'\n\nโฅ ษดแดแดแด : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nโฅ แด๊ฑแดสษดแดแดแด : @{msg.forward_from["username"]} \n\nโฅ ษชแด : <code>{msg.forward_from["id"]}</code>\n\nโฅ แดแด : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nโฅ ษชแด : `{msg.forward_from["id"]}`\n\n\n\nโฅ แดแด : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"โผ๏ธแดสสแดส <b><i>{hidden}</i></b> โผ๏ธแดสสแดส",
                quote=True,
            )
        else:
            text = f"<u>๐๐ข๐ฅ๐ช๐๐ฅ๐ ๐จ๐ฆ๐๐ฅ๐ก๐๐ ๐</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>๐๐๐๐ก๐ก๐๐</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>๐๐ฅ๐ข๐จ๐ฃ</u>"
            text += f'\n\nโฅ ษดแดแดแด {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nโฅ แด๊ฑแดสษดแดแดแด : @{msg.forward_from_chat["username"]}'
                text += f'\n\nโฅ ษชแด : `{msg.forward_from_chat["id"]}`\n\nโฅ แดแด : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nโฅ ษชแด `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









