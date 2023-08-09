from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

from agents import linkedin_lookup_agent, twitter_lookup_agent
from third_parties import linkedin
from third_parties.twitter import scrape_user_tweets

name = "Bao Loc Tong"
if __name__ == "__main__":
    print("Hello LangChain!")

    linkedin_profile_url = linkedin_lookup_agent.lookup(name) # -> Linkedin link
    linkedin_data = linkedin.get_linkedin_data(linkedin_profile_url) # json

    twitter_username = "Bao Loc"  # twitter_lookup_agent.lookup(name) # -> Twitter username
    tweets = scrape_user_tweets(twitter_username, num_tweets=5)  # json

    summary_template = """given the Linkedin information {linkedin_information} and twitter {twitter_information} 
    about a person from I want you to create: 1. a short summary 2. two interesting facts about them 3. A topic that 
    may interest them 4. 2 creative Ice breakers to open a conversation with them"""

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(linkedin_information=linkedin_data, twitter_information=tweets)

    print(result)