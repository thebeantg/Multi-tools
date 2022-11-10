import asyncio
import pyrogram
from plugins import txt as tg
from plugins.utils.http import get
from plugins.font_btn import style_btn_back, nxt_fonts_nxt, style_btn_editz
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery                            

from image.edit_1 import (bright, mix, black_white, g_blur, normal_blur, box_blur)
from image.edit_2 import (circle_with_bg, circle_without_bg, sticker, edge_curved, contrast, sepia_mode, pencil, cartoon)                              
from image.edit_3 import (green_border, blue_border, black_border, red_border)
from image.edit_4 import (rotate_90, rotate_180, rotate_270, inverted, round_sticker, removebg_white, removebg_plain, removebg_sticker)
from image.edit_5 import (normalglitch_1, normalglitch_2, normalglitch_3, normalglitch_4, normalglitch_5, scanlineglitch_1, scanlineglitch_2, scanlineglitch_3, scanlineglitch_4, scanlineglitch_5)                             
 

@Client.on_callback_query()
async def callback(client: Client, query: CallbackQuery): 
    if query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif query.data == "start":
       await query.message.edit(
           text = tg.STAT.format(query.from_user.mention),        
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("ʜᴇʟᴩ & ᴄᴍᴅꜱ", callback_data="help"),
               InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", callback_data="source")
               ],[            
               InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ", url="https://t.me/Hellbotsupport"),
               InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/hell_botz")
               ],[
               InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")   
               ]]
               )
       )
    elif query.data == "help":
        buttons = [[                           
            InlineKeyboardButton('ɪɴꜰᴏ & ɪᴅ', callback_data='info')
            ],[
            InlineKeyboardButton('ʟᴏɢᴏ ᴍᴀᴋᴇʀ', callback_data='logomake'),            
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴩʜ', callback_data='tgraph')
            ],[
            InlineKeyboardButton('ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ', callback_data='tts'),
            InlineKeyboardButton('yᴏᴜᴛᴜʙᴇ ᴅʟ', callback_data='ytdl')
            ],[
            InlineKeyboardButton('ᴩʜᴏᴛᴏ ᴛᴏᴏʟ', callback_data='phediter'),
            InlineKeyboardButton('ᴩᴀꜱᴛᴇ ᴄᴏᴅᴇ', callback_data='paster')
            ],[
            InlineKeyboardButton('ꜱᴛɪᴄᴋᴇʀ ᴛᴏᴏʟ', callback_data='stickertool'),
            InlineKeyboardButton('ꜰᴏɴᴛ ꜱᴛyʟᴇ', callback_data='fontstyle')            
            ],[
            InlineKeyboardButton('ᴄᴀʀʙᴏɴ', callback_data='carben'),
            InlineKeyboardButton('ꜰᴜɴ ɢᴀᴍᴇ', callback_data='fun')                      
            ],[
            InlineKeyboardButton('◁', callback_data='start'),
                       
        ]]
        await query.message.edit_text(                     
            text=tg.HELP,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode='html'
        )
    
    elif query.data == "info":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.INFO,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )       
    elif query.data == "logomake":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.LOGO,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "tgraph":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.TELE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )   
    elif query.data == "tts":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.TTS,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )   
    elif query.data == "ytdl":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.YTDL,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "phediter":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.IMAGE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "paster":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.PASTE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "carben":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.CARB_TXT,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "stickertool":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.STICKER,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "fontstyle":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]    
       await query.message.edit(
           text=tg.FONT,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "fun":
       buttons = [[
           InlineKeyboardButton("◁", callback_data="help"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.FUN,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'      
       )    
    elif query.data == "about":       
       buttons = [[
           InlineKeyboardButton("◁", callback_data="start"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.ABT.format(v=__version__, bot=client.mention),
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='html'           
       )            
    elif query.data == "source":
       users = await get("https://api.github.com")
       list_of_users = ""
       count = 1
       for user in users:
           list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")       
           count += 1
       buttons = [[
           InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/about_beantg"),
           InlineKeyboardButton("ʜᴇʟʟ ʙᴏᴛᴢ", url="https://t.me/hell_botz")
           ],[
           InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://graph.org/file/93c32d542399597c005e4.jpg"),
           ],[
           InlineKeyboardButton("◁", callback_data="start"),
           InlineKeyboardButton("↻ ᴄʟᴏꜱᴇ ↻", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.SOURCE.format(dev=list_of_users),
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode='markdown'
       )    
    elif query.data == "removebg":
       await query.message.edit_text(
           text="**Select required mode**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Wɪᴛʜ ᴡʜɪᴛᴇ ʙɢ", callback_data="rmbgwhite"),
               InlineKeyboardButton(text="Wɪᴛʜᴏᴜᴛ ʙɢ", callback_data="rmbgplain"),
               ],[
               InlineKeyboardButton(text="Sᴛɪᴄᴋᴇʀ", callback_data="rmbgsticker"),
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]
           )
       )
    elif query.data == "stick":
       await query.message.edit(
           text="**Select a Type**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Nᴏʀᴍᴀʟ", callback_data="stkr"),
               InlineKeyboardButton(text="Eᴅɢᴇ ᴄᴜʀᴠᴇᴅ", callback_data="cur_ved"),
               ],[                    
               InlineKeyboardButton(text="Cɪʀᴄʟᴇ", callback_data="circle_sticker")
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]                
           )
       )
    elif query.data == "rotate":
       await query.message.edit_text(
           text="**Select the Degree**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="180", callback_data="180"),
               InlineKeyboardButton(text="90", callback_data="90")
               ],[
               InlineKeyboardButton(text="270", callback_data="270")
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]
           )
       )
    elif query.data == "glitch":
       await query.message.edit_text(
           text="**Select required mode**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Nᴏʀᴍᴀʟ", callback_data="normalglitch"),
               InlineKeyboardButton(text="Sᴄᴀɴ ʟᴀɪɴᴀ", callback_data="scanlineglitch")
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]
           )
       )
    elif query.data == "normalglitch":
       await query.message.edit_text(
           text="**Select Glitch power level**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="1", callback_data="normalglitch1"),
               InlineKeyboardButton(text="2", callback_data="normalglitch2"),
               InlineKeyboardButton(text="3", callback_data="normalglitch3"),
               ],[
               InlineKeyboardButton(text="4", callback_data="normalglitch4"),
               InlineKeyboardButton(text="5", callback_data="normalglitch5"),
               ],[
               InlineKeyboardButton('◁', callback_data='glitch')
               ]]
           )
       )
    elif query.data == "scanlineglitch":
       await query.message.edit_text(
           text="**Select Glitch power level**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
               InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
               InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
               ],[
               InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
               InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
               ],[
               InlineKeyboardButton('◁', callback_data='glitch')
               ]]
           )
       )
    elif query.data == "blur":
       await query.message.edit(
           text="**Select a Type**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Bᴏx", callback_data="box"),
               InlineKeyboardButton(text="Nᴏʀᴍᴀʟ", callback_data="normal"),
               ],[
               InlineKeyboardButton(text="Gᴀᴜꜱꜱɪᴀɴ", callback_data="gas")
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]
           )
       )
    elif query.data == "circle":
       await query.message.edit_text(
           text="**Select required mode**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Wɪᴛʜ ʙɢ", callback_data="circlewithbg"),
               InlineKeyboardButton(text="Wɪᴛʜᴏᴜᴛ ʙɢ", callback_data="circlewithoutbg"),
               ],[
               InlineKeyboardButton('◁', callback_data='photo')
               ]]
           )
       )
    elif query.data == "border":
       await query.message.edit(
           text="**Select Border**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="Rᴇᴅ", callback_data="red"),
               InlineKeyboardButton(text="Gʀᴇᴇɴ", callback_data="green"),
               ],[
               InlineKeyboardButton(text="Bʟᴀᴄᴋ", callback_data="black"),
               InlineKeyboardButton(text="Bʟᴜᴇ", callback_data="blue"),
               ],[                    
               InlineKeyboardButton('◁', callback_data='photo')   
               ]]                
           )
       )
    elif query.data == "bright":
        await bright(client, query.message)
    elif query.data == "mix":
        await mix(client, query.message)
    elif query.data == "b|w":
        await black_white(client, query.message)
    elif query.data == "circlewithbg":
        await circle_with_bg(client, query.message)
    elif query.data == "circlewithoutbg":
        await circle_without_bg(client, query.message)
    elif query.data == "green":
        await green_border(client, query.message)
    elif query.data == "blue":
        await blue_border(client, query.message)
    elif query.data == "red":
        await red_border(client, query.message)
    elif query.data == "black":
        await black_border(client, query.message)
    elif query.data == "circle_sticker":
        await round_sticker(client, query.message)
    elif query.data == "inverted":
        await inverted(client, query.message)
    elif query.data == "stkr":
        await sticker(client, query.message)
    elif query.data == "cur_ved":
        await edge_curved(client, query.message)
    elif query.data == "90":
        await rotate_90(client, query.message)
    elif query.data == "180":
        await rotate_180(client, query.message)
    elif query.data == "270":
        await rotate_270(client, query.message)
    elif query.data == "contrast":
        await contrast(client, query.message)
    elif query.data == "box":
        await box_blur(client, query.message)
    elif query.data == "gas":
        await g_blur(client, query.message)
    elif query.data == "normal":
        await normal_blur(client, query.message)
    elif query.data == "sepia":
        await sepia_mode(client, query.message)
    elif query.data == "pencil":
        await pencil(client, query.message)
    elif query.data == "cartoon":
        await cartoon(client, query.message)
    elif query.data == "normalglitch1":
        await normalglitch_1(client, query.message)
    elif query.data == "normalglitch2":
        await normalglitch_2(client, query.message)
    elif query.data == "normalglitch3":
        await normalglitch_3(client, query.message)
    elif query.data == "normalglitch4":
        await normalglitch_4(client, query.message)
    elif query.data == "normalglitch5":
        await normalglitch_5(client, query.message)
    elif query.data == "scanlineglitch1":
        await scanlineglitch_1(client, query.message)
    elif query.data == "scanlineglitch2":
        await scanlineglitch_2(client, query.message)
    elif query.data == "scanlineglitch3":
        await scanlineglitch_3(client, query.message)
    elif query.data == "scanlineglitch4":
        await scanlineglitch_4(client, query.message)
    elif query.data == "scanlineglitch5":
        await scanlineglitch_5(client, query.message)
    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)
    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)
    elif query.data == "rmbgsticker":
        await removebg_sticker(client, query.message)
    elif query.data == "photo":
        buttons = [[
            InlineKeyboardButton(text="Bʀɪɢʜᴛ", callback_data="bright"),
            InlineKeyboardButton(text="Mɪxᴇᴅ", callback_data="mix"),
            InlineKeyboardButton(text="Bʟᴀᴄᴋ & ᴡʜɪᴛᴇ", callback_data="b|w"),
            ],[
            InlineKeyboardButton(text="Cɪʀᴄʟᴇ", callback_data="circle"),
            InlineKeyboardButton(text="Bʟᴜʀ", callback_data="blur"),
            InlineKeyboardButton(text="Bᴏʀᴅᴇʀ", callback_data="border"),
            ],[
            InlineKeyboardButton(text="Sᴛɪᴄᴋᴇʀ", callback_data="stick"),
            InlineKeyboardButton(text="Rᴏᴛᴀᴛᴇ", callback_data="rotate"),
            InlineKeyboardButton(text="Cᴏɴᴛʀᴀꜱᴛ", callback_data="contrast"),
            ],[
            InlineKeyboardButton(text="Sᴇᴩɪᴀ", callback_data="sepia"),
            InlineKeyboardButton(text="Pᴇɴᴄɪʟ", callback_data="pencil"),
            InlineKeyboardButton(text="Cᴀʀᴛᴏᴏɴ", callback_data="cartoon"),
            ],[
            InlineKeyboardButton(text="Iɴᴠᴇʀᴛ", callback_data="inverted"),
            InlineKeyboardButton(text="Gʟɪᴛᴄʜ", callback_data="glitch"),
            InlineKeyboardButton(text="Rᴇᴍᴏᴠᴇ ʙɢ", callback_data="removebg")
            ],[
            InlineKeyboardButton(text="◁", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)        
        await query.message.edit_text(        
            text="Select your required mode from below!",
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "nxt":
       await nxt_fonts_nxt(client, query)
    elif query.data == "fontblack":
       await style_btn_back(client, query)    
    elif "style" in query.data:
       cmd, style = query.data.split('+')
       await style_btn_editz(client, query, style) 




               
