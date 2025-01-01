import os
from langchain_google_genai import ChatGoogleGenerativeAI
from scripts.utils import get_api_key

# get gemini api key
gemini_api = get_api_key('GEMINI_API_KEY')

# Define LLM settings for agent
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        verbose=True,
        temperature=0.7,
        google_api_key=gemini_api,
    )
except Exception as e:
    print(f"Error initializing ChatGoogleGenerativeAI: {e}")
    raise

# Additional agent specific settings
AGENT_SETTINGS = {
    "researcher": {
        "llm": llm,
    },
    "writer": {
        "llm": llm,
    },
    "critic": {
        "llm": llm,
    },
}