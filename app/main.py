from chatbot.chatbot import Chatbot


def main():

    chatbot = Chatbot()

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye 👋")
            break

        response = chatbot.chat(user_input)

        print(f"\nGemma: {response}")


if __name__ == "__main__":
    main()