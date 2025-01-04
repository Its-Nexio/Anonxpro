import requests
from AnonXMusic import app
from pyrogram.types import Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

API_KEY = "abc921ff654bcf7b3faff8f775d781d8d27d32bfd02d6692eea30249ba781c8b"
BASE_URL = "https://api.together.xyz/v1/chat/completions"

@app.on_message(
    filters.command(
        ["chatgpt", "ai", "ask", "gpt", "solve"],
        prefixes=["+", ".", "/", "-", "", "$", "#", "&"],
    )
)
async def chat_gpt(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "❍ ᴇxᴀᴍᴘʟᴇ:**\n\n/chatgpt ᴡʜᴏ ɪs ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ˹ ʙʙʏ-ᴍᴜsɪᴄ ™˼𓅂?"
            )
        else:
            query = message.text.split(' ', 1)[1]
            print("Input query:", query)
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
            response = requests.post(BASE_URL, json=payload, headers=headers)

            print("API Response Text:", response.text)  # Print raw response
            print("Status Code:", response.status_code)  # Check the status code

            # If the response is empty or not successful, handle the error
            if response.status_code != 200:
                await message.reply_text(f"❍ ᴇʀʀᴏʀ: API request failed. Status code: {response.status_code}")
            elif not response.text.strip():
                await message.reply_text("❍ ᴇʀʀᴏʀ: API se koi valid data nahi mil raha hai. Response was empty.")
            else:
                # Attempt to parse the JSON response
                try:
                    response_data = response.json()
                    print("API Response JSON:", response_data)  # Debug response JSON

                    # Get the assistant's response from the JSON data
                    if "choices" in response_data and len(response_data["choices"]) > 0:
                        result = response_data["choices"][0]["message"]["content"]
                        await message.reply_text(
                            f"{result} \n\n❍ᴘᴏᴡᴇʀᴇᴅ ʙʏ➛[sᴛʀᴀɴɢᴇʀ™](https://t.me/SHIVANSH474)",
                            parse_mode=ParseMode.MARKDOWN
                        )
                    else:
                        await message.reply_text("❍ ᴇʀʀᴏʀ: No response from API.")
                except ValueError:
                    await message.reply_text("❍ ᴇʀʀᴏʀ: Invalid response format.")
    except Exception as e:
        # Catch any other exceptions and send an error message
        await message.reply_text(f"**❍ ᴇʀʀᴏʀ: {e} ")
