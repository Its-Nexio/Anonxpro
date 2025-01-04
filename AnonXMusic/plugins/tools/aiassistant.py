from pyrogram import Client, filters, enums
import requests
import urllib.parse
import asyncio
from pyrogram.types import Message
from AnonXMusic import app

def ask_query(query, model=None):
    default_model = 'gpt-4o'
    system_prompt = """ʏᴏᴜ ᴀʀᴇ ᴀ ʜᴇʟᴘғᴜʟ ᴀssɪsᴛᴀɴᴛ. ᴍʏ ɴᴀᴍᴇ ɪs sᴀᴘɴᴀ ᴀɪ, ᴀɴᴅ ᴍᴜ ᴏᴡɴᴇʀ ɴᴀᴍᴇ ɪs sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ, ᴋɴᴏᴡɴ ᴀs : @itzAsuraa """

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nᴜsᴇʀ: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://darkness.ashlynn.workers.dev/chat/?prompt=${encodeURIComponent(prompt)}&model=meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"ᴇʀʀᴏʀ : ғᴇᴛᴄʜɪɴɢ ʀᴇsᴘᴏɴsᴇ ғʀᴏᴍ ᴀᴘɪ. sᴛᴀᴛᴜs ᴄᴏᴅᴇ : {response.status_code}"

async def send_typing_action(client: Client, chat_id: int, duration: int = 1):
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)

def get_model_from_db(group_id):
    return 'claude-sonnet-3.5'
@app.on_message(filters.command(["apna", "chatgpt", "i", "ask", "gpt", "solve"], prefixes=["A", "S", "+", ".", "/", "-", ":", "$", "#", "&"]))
async def handle_query(client, message):
    if len(message.command) < 2:
        await message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention
    await send_typing_action(client, message.chat.id, duration=2)
    response = ask_query(user_query)
    await message.reply_text(f"{user_mention}, <b>{response}</b>")

@app.on_message(filters.mentioned & filters.group)
async def handle_mention(client: Client, message: Message) -> None:
    group_id = message.chat.id

    user_text = None

    if message.reply_to_message and message.reply_to_message.text:
        user_text = message.reply_to_message.text.strip()
    elif len(message.text.split(" ", 1)) > 1:
        user_text = message.text.split(" ", 1)[1].strip()

    if user_text:
        model_name = get_model_from_db(group_id)

        await send_typing_action(client, group_id)

        api_response = ask_query(user_text, model_name)

        await message.reply(f"<b>{api_response}</b>")
    else:
        await message.reply("<b>ᴘʟᴇᴀsᴇ ᴀsᴋ ᴀ ǫᴜᴇsᴛɪᴏɴ ᴀғᴛᴇʀ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴍᴇ</b>")
