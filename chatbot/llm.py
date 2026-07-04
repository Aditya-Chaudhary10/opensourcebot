from langchain_ollama import ChatOllama

from app.config import settings

def get_llm()-> ChatOllama:
    '''
    Create and return a configured Chatollama instance.
    '''

    return ChatOllama(
        model=settings.model_name,
        base_url=settings.ollama_base_url,
        temperature=settings.temperature
    )