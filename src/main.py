from agents.researcher import researcher, research
from crewai import Crew, Process

if __name__ == "__main__":
    crew = Crew(
        agents=[researcher],
        tasks=[research],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()