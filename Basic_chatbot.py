def get_reply(message):
    """Return a response to a simple user message."""
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi! How can I help you?"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks! How are you?"
    elif message in ("i am fine", "i'm fine", "fine"):
        return "Glad to hear that!"
    elif message in ("what is your name", "what is your name?"):
        return "I'm CodeAlpha Bot, a simple Python chatbot."
    elif message in ("help", "what can you do"):
        return "I can reply to greetings, simple questions, and goodbye messages."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return None
    else:
        return "Sorry, I don't understand that yet. Try saying 'hello' or 'help'."

def main():
    print("=== CodeAlpha Basic Chatbot ===")
    print("Type 'bye' to end the conversation.")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)

        if reply is None:
            print("Bot: Goodbye! Have a nice day.")
            break

        print("Bot:", reply)

if __name__ == "__main__":
    main()
