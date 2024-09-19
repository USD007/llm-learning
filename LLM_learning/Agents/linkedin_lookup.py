import os
from dotenv import load_dotenv
from langchain_community.llms.anyscale import create_llm_result
from langchain_ollama import ChatOllama
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from LLM_learning.tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub

def lookup(name: str) -> str:
    #llm = ChatOllama(model="llama3")
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    #print(os.getenv("TAVILY_API_KEY"))
    template = """given the full name {name_of_person} I want you to get  me a link to their Linkedin profile page.
    before making a decision check if they have atleast 50 followers to verify and also the name is case insensitive
                     Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(name="Crawl google 4 linkedin profile page",
             func=get_profile_url_tavily,
             description="useful for when you need get the Linkedin Page URL", )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_in_url = result["output"]
    return linked_in_url

if __name__ == '__main__':
    linkedin_url = lookup("ujwal d")
    print(linkedin_url)


