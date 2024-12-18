from agents.researcher import researcher, research
from agents.writer import writer, writing
from crewai import Crew, Process

if __name__ == "__main__":
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research, writing],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()