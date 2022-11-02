from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from helper.fsub import ForceSub 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.add_new import add_user
from variables import PICS, ADMIN
from plugins.utils.logo_maker import generate_logo
import asyncio
import random
import time
from helper.errors import capture_err
from plugins.utils.http import get
form plugins import txt

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    await add_user(bot, message)               
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi Featured Bot With Many Variety Features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id, Sticker id, kang, and others, etc...\nYou can see My commands by below button...",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")               
            ]]
            )
        )
       
         
                                     
@Client.on_message(filters.command(["id", "info"], ["/", "."]))
async def media_info(bot, m): 
    FSub = await ForceSub(bot, m)
    if FSub == 400:
        return
    message = m
    ff = m.from_user
    md = m.reply_to_message
    if md:
       try:
          if md.photo:
              await m.reply_text(text=f"**your photo id is **\n\n`{md.photo.file_id}`") 
          if md.sticker:
              await m.reply_text(text=f"**your sticker id is **\n\n`{md.sticker.file_id}`")
          if md.video:
              await m.reply_text(text=f"**your video id is **\n\n`{md.video.file_id}`")
          if md.document:
              await m.reply_text(text=f"**your document id is **\n\n`{md.document.file_id}`")
          if md.audio:
              await m.reply_text(text=f"**your audio id is **\n\n`{md.audio.file_id}`")
          if md.text:
              await m.reply_text("**hey man please reply with ( photo, video, sticker, documents, etc...) Only media **")  
          else:
              print("[404] Error..🤖]")                                                                                      
       except Exception as e:
          print(e)
                                        
    if not md:
        buttons = [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
        ],[            
        await m.reply("please wait....")
        await asyncio.sleep(3)
        if ff.photo:
           user_dp = await bot.download_media(message=ff.photo.big_file_id)
           await m.reply_photo(
               photo=user_dp,
               caption=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode="html",
               disable_notification=True
           )          
           os.remove(user_dp)
        else:  
           await m.reply_text(
               text=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode="html",
               disable_notification=True
           )


@Client.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logosq(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    try:
      text = message.text.replace("logosq","").replace("/","").replace("[ᗷETᗩ]","").strip().upper()
      
      if text == "":
        return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETA\n/logosq BETA")
  
      x = await message.reply_text("`🔍 Generating Logo For You...`")  
      logo = await generate_logo(text,True)
  
      if "graph.org" not in logo:
        return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In [SUPPORT GRP](t.me/beta_support).")
        
      if "error" in logo:
        return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [SUPPORT GRP](t.me/beta_support). \n\n`{logo}`")
        
      await x.edit("`🔄 Done Generated... Now Sending You`")
      
      logo_id = logo.replace("https://graph.org//file/","").replace(".jpg","").strip()
      
      await message.reply_photo(logo,caption = "**🖼 Logo Generated By TG-MULTI-BOT**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    except FloodWait:
      pass
    except Exception as e:
      try:
        await x.delete()
      except:
        pass
      return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")

@Client.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logo(bot, message):
  FSub = await ForceSub(bot, message)
  if FSub == 400:
      return 
  try:
    text = message.text.replace("logo","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETAs\n/logosq MKN")

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "graph.org" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In  [SUPPORT GRP](t.me/beta_support).")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [SUPPORT GRP](t.me/beta_support).\n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://graph.org//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption = "**🖼 Logo Generated By TG-MULTI-BOT**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")


@Client.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://graph.org//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By [ᗷETᗩ]**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()



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

    

