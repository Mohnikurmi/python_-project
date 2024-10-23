def chatbot_response(user_input):
    """Basic responses based on user input."""
    user_input = user_input.lower()

    # Basic greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Bot identity response
    elif "who are you" in user_input or "what is your name" in user_input:
        return "I am a simple chatbot created to assist you with basic questions."

    # Asking how the user is
    elif "how are you" in user_input:
        return "I'm just a program, but thank you for asking! How about you?"

    # Thank you response
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! I'm happy to help."

    # Default fallback response for unrecognized input
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase?"


def chat():
    """Main chat function to handle conversation loop."""
    print("Chatbot: Hello! I am here to assist you. Type 'bye' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get chatbot's response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()

