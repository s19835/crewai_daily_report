import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Process, Crew

# get the gemini api key from env
api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise ValueError("Api key is not set in the env variable!")

