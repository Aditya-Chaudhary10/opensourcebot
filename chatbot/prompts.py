from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

basic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant.",
        ),

        MessagesPlaceholder(variable_name="history"),

        (
            "human",
            "{question}",
        ),
    ]
)