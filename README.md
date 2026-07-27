# API Explorer Chatbot

A simple command-line chatbot built with Python that uses the NVIDIA NIM API to chat with an LLM and saves conversation history between sessions.

## Features

- Chat with an LLM using the NVIDIA NIM API
- Saves and reloads conversation history
- Handles common errors (API key, network, invalid history, empty input)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file:
   ```env
   NVIDIA_API_KEY=your_api_key_here
   ```

3. Run the chatbot:
   ```bash
   python chatbot.py
   ```

Type `quit` to exit. Conversation history is automatically saved.
