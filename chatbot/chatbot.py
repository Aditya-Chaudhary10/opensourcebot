from chatbot.llm import get_llm
from chatbot.prompts import basic_prompt

from langchain_core.messages import HumanMessage,AIMessage

class Chatbot:

    def __init__(self):
        self.llm=get_llm()

        self.messages=[]

    def chat(self, question:str)-> str:

        self.messages.append(
            HumanMessage(content=question)
        )



        prompt=basic_prompt.invoke(
            {
                'history':self.messages,
                'question':question
            }
        )

        response=self.llm.invoke(prompt.messages)

        self.messages.append(
            AIMessage(content=response.content)
        )

        print("\nConversation History:")
        print(self.messages)

        return response.content