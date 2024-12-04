import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Process, Crew
from langchain_community.tools import DuckDuckGoSearchRun

def main():
    # get the gemini api key from env
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key is None:
        raise ValueError("Api key is not set in the env variable!")

    # create llm using gemini pro
    llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.6, api_key=api_key)
    
    # setup a tool
    search_tool = DuckDuckGoSearchRun()
    
    # define agents with roles and goals
    
    # define researcher for doing research for the concepts
    researcher = Agent(
        role='Senior Research Analysist',
        goal='Uncover cutting-edge developments in AI and data science',
        backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[
            search_tool
        ]
    )

    # define writer agent for writing the research results
    writer = Agent(
        role='Tech Content Strategist',
        goal='Craft compelling content on tech advancements',
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.""",
        verbose=True,
        allow_delegation=False,
        tools=[]
    )

if __name__ == "__main__":
    main()
