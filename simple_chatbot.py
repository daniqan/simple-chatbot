from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key) # Initialize OpenAI client with your API key
message_log = [{"role": "system", "content": "You are a helpful assistant."}] # System message

def chatbot_response(user_message):
    message_log.append({"role": "user", "content": user_message})  # Add user message to log
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Affordable model for beginners
        messages=message_log
    )
    reply = response.choices[0].message.content  # Get the bot's reply
    message_log.append({"role": "assistant", "content": reply})  # Add bot reply to log
    return reply 

# Interactive loop
print("Chatbot ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    reply = chatbot_response(user_input)
    print("Bot:", reply)