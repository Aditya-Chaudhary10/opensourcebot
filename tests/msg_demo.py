from langchain_core.messages import HumanMessage, SystemMessage

from chatbot.llm import get_llm

llm = get_llm()

messages = [
    SystemMessage(
        content="You are a pirate. Every answer should sound like a pirate."
    ),
    HumanMessage(
        content="Hello, who are you?"
    )
]

response = llm.invoke(messages)

print(response.content)