import requests
import urllib.parse

def get_chat_response(prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://darkness.ashlynn.workers.dev/chat/?prompt={encoded_prompt}"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

prompt_text = "Hello, how are you?"
response = get_chat_response(prompt_text)

if response:
    print("Response from server:", response)
