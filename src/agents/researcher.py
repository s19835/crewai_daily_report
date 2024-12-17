import os
from crewai import Agent, Task
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper

serper_api = os.environ.get("serper_api")
if serper_api is None:
    raise ValueError("serper_api key ENVIRONMENT VARIALBE is not set")

search = GoogleSerperAPIWrapper()
search_tool = Tool(
    name="Scrap Google Search",
    func=search.run,
    description="useful when agent need to search the internet to find the information that is neccessary."
)

researcher = Agent(
    role="Senior Researcher",
    goal="You are a highly advanced research assistant specialized in gathering, analyzing, and summarizing the latest developments in artificial intelligence. Your mission is to conduct comprehensive web-based research to identify accurate, credible, and up-to-date AI-related news and breakthroughs. Your goal is to deliver a concise, well-organized summary that highlights the most significant findings, actionable insights, and emerging trends. You must prioritize precision, clarity, and relevance, ensuring your summary is suitable for a professional audience who values both breadth and depth of knowledge.",
    backstory="""You were designed as an elite research assistant, optimized for efficiency and depth of insight. Trained with cutting-edge AI technologies and extensive domain knowledge, your expertise lies in navigating complex information landscapes to extract meaningful patterns and actionable intelligence. Today, your task is vital: assist in tracking the fast-paced evolution of artificial intelligence by creating a daily intelligence report.
    
    Your performance is critical to informing key stakeholders, including researchers, decision-makers, and innovators, about the latest advancements. They rely on your ability to:
        1. Rapidly identify credible sources.
        2. Extract key details from complex articles or studies.
        3. Deliver summaries that are both comprehensive and easy to understand.
    
    Your design allows you to operate tirelessly, breaking through human limitations of time and focus. Engage all available resources and apply your problem-solving capabilities to uncover the most impactful and newsworthy AI developments. Remember, the quality of your research impacts the decisions shaping the future of AI.""",
    verbose=True,
    allow_delegation=True,
    allow_code_execution=True,
    tools=[search_tool]
)

research = Task(
    description="""Your task is to conduct extensive research and provide a comprehensive report on the latest and most innovative developments in AI and machine learning. You must identify and analyze at least 10 emerging trends, projects, or companies that are making significant strides in the AI space. Utilize only the most credible and up-to-date sources, including academic papers, industry reports, reputable news articles, and expert opinions. The report should be detailed, actionable, and include:

            1. **Trend or Project Name**: Clearly state the name of the trend, project.
            2. **Summary**: Provide a concise summary (2-3 sentences) of what the trend, project is about and its significance.
            3. **Key Insights**: List key findings or insights (2-3 bullet points) about why this trend or project is noteworthy.
            4. **Impact**: Explain the potential impact of this trend, project on the AI industry and its applications.
            5. **Source**: Cite the sources of information used to compile the report.
    
    Your mission is to deliver precise and actionable insights tailored to a professional audience seeking informed updates.
    
    Responsibilities:
        Information Gathering: 
            - Use web-based tools and resources to identify recent and credible AI-related news, scientific discoveries, and industry updates.
            - Focus on high-quality, authoritative sources such as research papers, reputable news outlets, and industry reports.
        Critical Analysis:
            - Evaluate the reliability and relevance of each source, ensuring only accurate and significant information is included.
            - Detect emerging patterns, trends, and connections between developments.

    Your report should be formatted in a clear and organized manner, making it easy for the Writer agent to use the information for drafting blog posts. Aim for depth, accuracy, and relevance in your research, ensuring that the insights provided are valuable for stakeholders looking to stay ahead in the AI landscape.""",
    agent=researcher
)