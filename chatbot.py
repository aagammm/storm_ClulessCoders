import openai

# Set your OpenAI API key
openai.api_key = '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'

# Initialize a conversation with a system message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]

# Function to get a chatbot response
def get_chatbot_response(user_input):
    # Add the user's message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Generate a response from the chatbot
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    # Extract and return the chatbot's reply
    chatbot_reply = response['choices'][0]['message']['content']
    return chatbot_reply

# Main interaction loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")

    # Exit the loop if the user enters 'exit' or 'quit'
    if user_input.lower() in ['exit', 'quit']:
        break

    # Get the chatbot's response
    chatbot_response = get_chatbot_response(user_input)

    # Display the chatbot's reply
    print("Chatbot:", chatbot_response)
