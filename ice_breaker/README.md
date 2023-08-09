https://www.udemy.com/course/langchain/learn/lecture/37491226#overview

github.com:emarco177/ice_breaker.git

 pip install --user pipenv

 pyenv shell 3.10.5 (python version) ???

pipenv shell 

pipenv install langchain

https://python.langchain.com/docs/get_started/introduction.html (dung de lam viec voi LLM)

pipenv install black (Black is the uncompromising Python code formatter.)

pipevn install openai


#####

10. Integrating Linkedin Data Processing - Part 1 - Scraping
  
Pull rich data about people and companies: | 

12. Linkedin Data Processing- Part 3: Tools, AgentType & initialize_agent
-- Create a new tools 
    help agent to intergrate with outside world
    sai serpapi.com de lay du lieu SERPAPI_API_KEY
-- Create a new agent type

-- Create a new agent

-- Create a new twitter third party agent
pipenv install tweepy

## External API
### Proxycurl is a proxy API that allows you to scrape the web without getting blocked. It's fast, easy to use, and reliable.
https://nubela.co/proxycurl/  


### SerpApi is a real-time API to access Google search results. We handle the issues of having to rent proxies, solving captchas, and JSON parsing in an easy to use and integrate API for our customers.
https://serpapi.com/

### Tweepy is a Python library for accessing the Twitter API.
Got forbidden issue when using tweepy
pipenv install tweepy
https://docs.tweepy.org/en/stable/
https://developer.twitter.com/en/portal/apps/4412269/settings

## Issues
### Got forbidden issue when using tweepy
453 - You currently have access to a subset of Twitter API v2 endpoints and limited v1.1 endpoints (e.g. media post, oauth) only. If you need access to this endpoint, you may need a different access level. You can learn more here: https://developer.twitter.com/en/portal/product
### Solution
Twitter has two versions of API, V 1 and V 2
We are using v1, However, We are using v2 access token.

api = tweepy.API (V1)

