

# Predefined chatbot responses
RESPONSES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! How can I help you?",
    "hey": "Hey! How can I help you?",
    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! How can I help you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "how's it going": "It's going great! Thanks for asking.",
    "how are you doing": "I'm doing great! Thanks for asking.",
    "nice to meet you": "Nice to meet you too!",
    "nice to see you": "Nice to see you too!",
    "what's up": "Not much! How can I help you?",
    "hey there": "Hey there! How can I help you?",
    "greetings": "Greetings! How can I help you?"
}

# Welcome message
print("=" * 40)
print("        Welcome to ChatBot")
print("=" * 40)
print("Type 'exit' anytime to end the conversation.\n")


# Start the chatbot
while True:

    # Get input from the user
    user_input = input("You: ")

    # Clean and normalize the user's input
    user_input = user_input.lower().strip()

    # Check for exit command
    if user_input == "exit":
        print("ChatBot: Goodbye! Thanks for chatting.")
        break

    # Find a matching response
    response = RESPONSES.get(
        user_input,
        "I'm sorry, I don't understand that. Please try another question."
    )

    # Display the chatbot's response
    print("ChatBot:", response)