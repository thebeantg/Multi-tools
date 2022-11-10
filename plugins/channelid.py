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
        text = "<u>𝗙𝗢𝗥𝗪𝗔𝗥𝗗 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>𝗕𝗢𝗧 𝗜𝗡𝗙𝗢</u>"
        else:
            text += "<u>𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢</u>"
        text += f'\n\n➥ ɴᴀᴍᴇ : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\n➥ ᴜꜱᴇʀɴᴀᴍᴇ : @{msg.forward_from["username"]} \n\n➥ ɪᴅ : <code>{msg.forward_from["id"]}</code>\n\n➥ ᴅᴄ : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\n➥ ɪᴅ : `{msg.forward_from["id"]}`\n\n\n\n➥ ᴅᴄ : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"‼️ᴇʀʀᴏʀ <b><i>{hidden}</i></b> ‼️ᴇʀʀᴏʀ",
                quote=True,
            )
        else:
            text = f"<u>𝗙𝗢𝗥𝗪𝗔𝗥𝗗 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>𝗖𝗛𝗔𝗡𝗡𝗘𝗟</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>𝗚𝗥𝗢𝗨𝗣</u>"
            text += f'\n\n➥ ɴᴀᴍᴇ {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\n➥ ᴜꜱᴇʀɴᴀᴍᴇ : @{msg.forward_from_chat["username"]}'
                text += f'\n\n➥ ɪᴅ : `{msg.forward_from_chat["id"]}`\n\n➥ ᴅᴄ : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\n➥ ɪᴅ `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









