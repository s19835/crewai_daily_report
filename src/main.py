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

    # create tasks for the agents

    # task1: conduct comprehensive analysis on the AI topic
    task1 = Task(
        description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
        Identify key trends, breakthrough technologies, and potential industry impacts.
        Your final answer MUST be a full analysis report""",
        agent=researcher
    )

    # task2: using provided insight develp a well structured blog post
    task2 = Task(
        description="""Using the insights provided, develop an engaging blog post that highlights the most significant AI advancements.
        Your post should be informative yet accessible, catering to a tech-savvy audience.
        Make it sound cool, avoid complex words so it doesn't sound like AI.
        Your final answer MUST be the full blog post of at least 4 paragraphs and MUST contain MORE THAN 100 WORDS.""",
        agent=writer
    )

if __name__ == "__main__":
    main()
