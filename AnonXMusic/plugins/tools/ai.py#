import random
import time
import requests
from AnonXMusic import app
from config import BOT_USERNAME, SUPPORT_CHAT, SUPPORT_CHANNEL
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from TheApi import api


SACHIN = [
    [
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=f"https://t.me/SANATANI_SUPPORT"),
        InlineKeyboardButton(text="˹ ᴜᴘᴅᴀᴛᴇ's ˼", url=f"https://t.me/TENSION_TECH"),
    ],
    [
        InlineKeyboardButton(text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/TensionxMusicBot?startgroup=true"),
    ],
]


@app.on_message(filters.command(["apna", "chatgpt", "i", "ask", "gpt", "solve"], prefixes=["a", "A", "s", "S", "+", ".", "/", "-", "+", "$", "#", "&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<b>⬤ ᴇxᴀᴍᴘʟᴇ ➠</b>\n\n<code>Anony Where is TajMahal ?</code>"
            )
        else:
            question = message.text.split(' ', 1)[1]
            response = api.chatgpt(question)
            bot_info = await bot.get_me()
            bot_name = bot_info.first_name
            bot_id = bot_info.id
            if response:
                end_time = time.time()
                telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                await message.reply_text(
                    f"⬤ {response.strip()} \n\n**⬤ ᴀɴsᴡᴇʀɪɴɢ ʙʏ ➠ [{bot_name}](tg://user?id={bot_id})**",
                    parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(SACHIN)
                )
            else:
                await message.reply_text("⬤ ɴᴏ ᴀɴsᴡᴇʀ ғᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ")
    except Exception as e:
        await message.reply_text(f"Error - {e}")
