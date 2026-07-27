import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get('NVIDIA_API_KEY')
invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"

if not API_KEY:
    raise ValueError("API key not found or invalid")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

def call_llm(messages):


    payload = {
        "messages": messages,
        "model": "meta/llama-3.1-8b-instruct"
    }

    try:
    
        response = requests.post(invoke_url,headers=headers, json=payload, stream=False)
        response.raise_for_status()
        response = response.json()['choices'][0]['message']['content']
        return response

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Unable to connect to the server. Please check your internet connection or try again later.")
    except requests.exceptions.HTTPError:
           if response.status_code == 429:
               raise RuntimeError("Rate limit exceeded. You've sent too many requests in a short period. Please wait a moment and try again.")
    except requests.exceptions.Timeout:
        raise RuntimeError("Requests timed out. Server took too long to respond")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")