from typing import Tuple

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from LLM_learning.Agents.twitter_lookup_agent import twitter_lookup
from LLM_learning.third_parties.linked_in import scrape_linkedin_profile
from LLM_learning.Agents.linkedin_lookup import lookup as linkedin_lookup_agent, lookup

from LLM_learning.third_parties.twitter import scrape_user_tweets

from outputparser import summary_parser, Summary, get_summary_format_instructions


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username,
    )

    #twitter_username = twitter_lookup(name=name)
    #tweets = scrape_user_tweets(username=twitter_username, mock=True)



    summary_template = """
    given the information about a person from linkedin {information},
    
    1. A short summary
    2. two interesting facts about them 

    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": get_summary_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    #res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})
    res = chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Harrison Chase")



