import os
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_api = os.environ.get('GEMINI_API_KEY')
if gemini_api is None:
    raise ValueError("gemini api key ENVIRONMENT VARIALBE is not set")

# Define LLM settings for agent
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.7,
    google_api_key=gemini_api,
)

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