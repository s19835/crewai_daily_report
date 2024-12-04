import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew
from langchain.agents import Tool

def main():
    # Load Gemini API key from environment variables
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("API key is not set in the environment variable!")

    # Set up LLM using Gemini Pro
    llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)

    # Initialize DuckDuckGo search tool

    # Researcher agent to perform AI research
    researcher = Agent(
        role='Researcher',
        goal='Discover the latest advancements in AI',
        backstory="A tech-savvy researcher skilled in gathering insights on cutting-edge topics.",
        llm=llm,
        tools=[]
    )

    # Writer agent to draft blog posts
    writer = Agent(
        role='Writer',
        goal='Write a blog post summarizing research findings',
        backstory="An experienced writer with a knack for turning complex topics into engaging blogs.",
        llm=llm
    )

    # Define tasks for agents
    research_task = Task(
        description="Research the latest trends and hot news in AI for 2024. Provide a detailed summary.",
        agent=researcher
    )
    write_task = Task(
        description="Create a blog post based on the research insights. Write at least 150 words.",
        agent=writer
    )

    # Create a crew to manage agents and tasks
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        verbose=True
    )

    # Execute the tasks
    results = crew.kickoff()

    # Display the output
    print("Final Results:")
    print(results)

if __name__ == "__main__":
    main()
