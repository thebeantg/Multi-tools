from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters

"""Edit ചെയ്യുന്നവനോട്.. നിന്റെ തന്ത അല്ല ഈ code ഉണ്ടാക്കിയത് """

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Bʀɪɢʜᴛ", callback_data="bright"),
                        InlineKeyboardButton(text="Mɪxᴇᴅ", callback_data="mix"),
                        InlineKeyboardButton(text="Bʟᴀᴄᴋ & ᴡʜɪᴛᴇ", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="Cɪʀᴄʟᴇ", callback_data="circle"),
                        InlineKeyboardButton(text="Bʟᴜʀ", callback_data="blur"),
                        InlineKeyboardButton(text="Bᴏʀᴅᴇʀ", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="Sᴛɪᴄᴋᴇʀ", callback_data="stick"),
                        InlineKeyboardButton(text="Rᴏᴛᴀᴛᴇ", callback_data="rotate"),
                        InlineKeyboardButton(text="Cᴏɴᴛʀᴀꜱᴛ", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="Sᴇᴩɪᴀ", callback_data="sepia"),
                        InlineKeyboardButton(text="Pᴇɴᴄɪʟ", callback_data="pencil"),
                        InlineKeyboardButton(text="Cᴀʀᴛᴏᴏɴ", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="Iɴᴠᴇʀᴛ", callback_data="inverted"),
                        InlineKeyboardButton(text="Gʟɪᴛᴄʜ", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="Rᴇᴍᴏᴠᴇ ʙɢ", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="↻ ᴄʟᴏꜱᴇ ↻", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return








