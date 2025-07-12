# A Simple Chatbot

This file guides you through a simple impletation of chatbot by wrapping OpenAI's ChatGPT LLM.

## Project Overview

This is a simple OpenAI-powered chatbot application written in Python. The project demonstrates basic ChatGPT integration using the OpenAI Python SDK v1.0+.

## Architecture

- `simple_chatbot.py` - Main chatbot implementation with interactive CLI loop and conversation memory
- `main.py` - Basic entry point (prints hello message)
- `pyproject.toml` - Project configuration and dependencies using uv package manager
- Environment-based configuration using `OPENAI_API_KEY`

## Development Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Set OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Running the Application
```bash
# Run the chatbot
python simple_chatbot.py

# Run the basic main script
python main.py
```

### Package Management
This project uses `uv` for dependency management. The main dependency is `openai>=1.95.0`.

## Key Implementation Details

The chatbot uses OpenAI's GPT-3.5-turbo model with a simple system prompt ("You are a helpful assistant"). The application:

- Maintains conversation history in `message_log` for context preservation
- Runs in an interactive loop where users can type messages and receive responses
- Exits when the user types 'exit'
- Handles API key management through environment variables for security

The `chatbot_response()` function handles message logging and API communication with OpenAI's chat completions endpoint.