from chatbot.llm import get_llm
from chatbot.prompts import basic_prompt

llm = get_llm()

chain = basic_prompt | llm

response = chain.invoke(
    {
        "history": [],
        "question": "What is LangChain?"
    }
)

print(response.content)