from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from AnonXMusic import app

class BUTTONS(object):
    ABUTTON = [
        [
            InlineKeyboardButton("ᴀɪ | ᴄʜᴀᴛɢᴘᴛ", callback_data="AI_BACK HELP_1"),
        ],
        [
            InlineKeyboardButton("ʙᴀɴ", callback_data="AI_BACK HELP_5"),
            InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="AI_BACK HELP_6"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="AI_BACK HELP_7"),
        ],
        [
            InlineKeyboardButton("ᴄᴀʀʙᴏɴ", callback_data="AI_BACK HELP_2"),
            InlineKeyboardButton("ᴛᴛs", callback_data="AI_BACK HELP_3"),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="AI_BACK HELP_4"),
        ],
        [
            InlineKeyboardButton("ɢʀᴀᴘʜ", callback_data="AI_BACK HELP_8"),
            InlineKeyboardButton("sɢ", callback_data="AI_BACK HELP_9"),
            InlineKeyboardButton("ᴡᴇʟ", callback_data="AI_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ᴢᴏᴍʙɪᴇ", callback_data="AI_BACK HELP_11"),
            InlineKeyboardButton("ɢ-ʙʏᴇ", callback_data="AI_BACK HELP_12"),
            InlineKeyboardButton("ᴍ-ᴀᴄᴛɪᴏɴ", callback_data="AI_BACK HELP_13"), 
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"settingsback_helper"),]
        ]
