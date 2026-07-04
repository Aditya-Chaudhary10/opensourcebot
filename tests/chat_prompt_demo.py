from chatbot.prompts import basic_prompt

prompt = basic_prompt.invoke(
    {
        "question": "What is LangChain?"
    }
)

print(prompt.messages)