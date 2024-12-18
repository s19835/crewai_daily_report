# **Crewai Daily Report**

Welcome to the `crewai_daily_report` project! This project leverages AI agents to automate the process of researching, writing, and critiquing daily reports on the latest AI trends.

## crewai

### How It All Works Together

- AI **Agents** work on their specialized tasks.
- **Tasks** get completed to achieve the goal.
- The **Crew** organizes the overall operation.
- The **Process** ensures smooth collaboration.

To learn more about crewai, head to the [documentation site](https://docs.crewai.com/introduction)

## **Project Overview**

The `crewai_daily_report` project consists of three AI agents: Researcher, Writer, and Critic, working sequentially to deliver high-quality articles on AI trends. Here's a brief overview of the process:

1. **Researcher Agent**: Gathers up-to-date information on the latest AI topics and trends.
2. **Writer Agent**: Uses the gathered information to draft a blog post or article.
3. **Critic Agent**: Reviews the draft, ensuring it meets quality standards and provides feedback for improvements.

This process is recurring, ensuring continuous production of relevant and insightful content.

## **File Structure**

The project is organized into the following structure:

```bash
crewai_daily_report/
├── LICENSE
├── README.md
├── requirements.txt
├── scripts/
│   ├── setup_env.py
│   ├── utils.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agents/
│   │   ├── researcher.py
│   │   ├── writer.py
│   │   ├── critic.py
│   ├── data/
│   │   ├── research/
│   │   ├── drafts/
│   │   ├── final/
│   ├── logs/
│   ├── config/
│   │   ├── llm_settings.py
├── .gitignore
├── .venv/
```

### **File and Folder Descriptions:**

#### **Root Directory**

- **`LICENSE`**: Contains the licensing information for the project.
- **`README.md`**: Provides an overview of the project, its purpose, setup instructions, and how to run it.
- **`requirements.txt`**: Lists all the dependencies and packages required to run the project.

#### **`scripts/`**

- **`setup_env.py`**: Script to set up the project environment, including installing dependencies and configuring paths.
- **`utils.py`**: Contains utility functions and common code that can be reused across the project.

#### **`src/`**

- **`__init__.py`**: Indicates that the directory is a Python package.
- **`main.py`**: The main script to initialize and run the entire process. It orchestrates the flow from the Researcher agent to the Writer and Critic agents.

##### **`src/agents/`**

- **`researcher.py`**: Contains the logic for the Researcher agent, responsible for gathering information about the latest AI trends and organizing this information for the Writer agent.
- **`writer.py`**: Contains the logic for the Writer agent, which takes the researched data and composes a draft blog post or article.
- **`critic.py`**: Contains the logic for the Critic agent, which reviews the Writer agent's drafts, checks for quality and adherence to guidelines, and provides feedback or approval.

##### **`src/data/`**

- **`research/`**: Stores the raw data and information collected by the Researcher agent.
- **`drafts/`**: Contains drafts written by the Writer agent awaiting review by the Critic agent.
- **`final/`**: Holds the final approved articles ready for publication or further distribution.

##### **`src/logs/`**

- Stores log files to track the processes, errors, and the performance of each agent for monitoring and debugging purposes.

#### **`.gitignore`**

- Specifies intentionally untracked files to ignore in Git. Typically includes files like environment configurations, logs, and compiled code.

#### **`venv/`**

- Virtual environment directory to manage dependencies locally without affecting the global Python installation.

---

## **How It Works**

(Details to be provided by the user.)

## **Installation**

(Details to be provided by the user.)

---
