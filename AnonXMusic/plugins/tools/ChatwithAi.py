from pyrogram import Client, filters
from pyrogram.types import Message
import openai
import asyncio

OPENAI_API_KEY = "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"  # Replace with your OpenAI API Key

openai.api_key = OPENAI_API_KEY

# Initialize Pyrogram client
app = Client("chatgpt_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Simulate typing action
async def send_typing_action(client, chat_id, duration=1):
    await client.send_chat_action(chat_id, "typing")
    await asyncio.sleep(duration)

# Function to process user query with ChatGPT
async def ask_gpt(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" if GPT-4 is unavailable
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=200,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Command handler for "/ask"
@app.on_message(filters.command("ask", prefixes=["/", ".", "!"]))
async def handle_query(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("<b>Please provide a query after the command.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing
    await send_typing_action(client, message.chat.id, duration=2)

    # Get response from ChatGPT
    response = await ask_gpt(user_query)

    # Send the response back to the user
    await message.reply_text(f"{user_mention}, <b>{response}</b>")

# Start the bot
if __name__ == "__main__":
    print("ChatGPT Bot is running...")
    app.run()
