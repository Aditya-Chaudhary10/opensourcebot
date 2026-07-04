from langchain_core.messages import BaseMessage,HumanMessage

messages=[]

messages.append(
    HumanMessage(content='Hi')
)

messages.append(
    HumanMessage(content='My name is Aditya')
)


print(messages)