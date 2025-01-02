from crewai import LLM
from langchain.agents import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from scripts.utils import get_api_key

# set up search tool for researcher
serper_api = get_api_key("SERPER_API_KEY")

search = GoogleSerperAPIWrapper()
search_tool = Tool(
    name="Scrap Google Search",
    func=search.run,
    description="useful when agent need to search the internet to find the information that is necessary."
)

# set up LLM for agents
gemini_api = get_api_key("GEMINI_API_KEY")
llm = LLM(
    model='gemini/gemini-pro',
    temperature=0.7,
    api_key=gemini_api
)