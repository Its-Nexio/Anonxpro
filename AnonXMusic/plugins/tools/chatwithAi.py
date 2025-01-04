import os, time
import openai
from AnonXMusic import app
from pyrogram import filters
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS
import requests, config

openai.api_key = "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"

@app.on_message(filters.command(["chatgpt","ai","ask"], prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app: app, message):
    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text("Hello! Please provide a question or message for the AI to respond to.")
        else:
            question = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "user", "content": question}], temperature=0.2)
            response_text = resp['choices'][0]["message"]["content"]
            await message.reply_text(response_text)

    except Exception as e:
        await message.reply_text(f"Error: {e}")
