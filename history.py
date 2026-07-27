import os
import json
from pathlib import Path

CONVERSATION_DIR = Path("conversations")
CONVERSATION_FILE = CONVERSATION_DIR / "chat1.json"


def load_history(path=CONVERSATION_FILE):
    if not path.exists():
        return [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    try:
        with open(path, "r", encoding="utf-8") as f:
            print(path)
            return json.load(f)

    except json.JSONDecodeError:
        print("Warning: Conversation history is corrupted. Starting a new conversation.")
        return [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    except OSError as e:
        print(f"Error reading conversation history: {e}")
        return [
            {"role": "system", "content": "You are a helpful assistant."}
        ]


def save_history(messages, path=CONVERSATION_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)
