from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key) # Initialize OpenAI client with your API key

def chatbot_response(user_message):
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # Affordable model for beginners
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # System prompt sets behavior
        {"role": "user", "content": user_message}  # User's input
    ])
    return response.choices[0].message.content

# Interactive loop
print("Chatbot ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    reply = chatbot_response(user_input)
    print("Bot:", reply)