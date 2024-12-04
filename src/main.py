import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Process, Crew

def main():
    # get the gemini api key from env
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key is None:
        raise ValueError("Api key is not set in the env variable!")

    # create llm using gemini pro
    llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.6, api_key=api_key)
    

if __name__ == "__main__":
    main()
