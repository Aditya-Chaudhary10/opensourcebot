from chatbot.prompts import basic_prompt

prompt=basic_prompt.invoke(
    {
        "question":'What is langchain'
    }
)

print(prompt.text)