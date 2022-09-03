from pyrogram import filters

from MULTIBOT import Client
from helper.errors import capture_err
from plugins.utils.http import get

__MODULE__ = "Repo"
__HELP__ = "/repo - To Get My Github Repository Link " "And Updates Channel Link"


@Client.on_message(filters.command("repo"))
async def repo(client, message):
    users = await get("https://api.github.com/repos/jeolpaul/TG-MULTI-BOT/contributors")
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")       
        count += 1
    text = f"""[Github](https://github.com/Jeolpaul/TG-MULTI-BOT) | [Updates](t.me/beta_botz)\n```----------------\n| Contributors |\n----------------```\n{list_of_users}"""
    await client.send_message(chat_id=message.chat.id, text=text, disable_web_page_preview=True)
