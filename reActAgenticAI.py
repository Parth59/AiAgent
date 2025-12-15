import os
from typing import Annotated, TypedDict
from dotenv import load_dotenv
import requests

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

# 1. Load secrets from .env
load_dotenv()

# 2. Define Tools
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """Fetches current weather data for a specific city."""
    # Pull key from environment instead of hardcoding
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    url = f'https://api.weatherstack.com/current?access_key={api_key}&query={city}'
    
    response = requests.get(url)
    data = response.json()
    
    if "current" in data:
        temp = data["current"]["temperature"]
        desc = data["current"]["weather_descriptions"][0]
        return f"The current weather in {city} is {desc} with a temperature of {temp}°C."
    return "Could not retrieve weather data."

# 3. Initialize the Model
# Using GPT-4o which is highly capable of multi-step tool use
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 4. Create the LangGraph Agent
# 'create_react_agent' is the modern replacement for AgentExecutor
tools = [search_tool, get_weather_data]
agent_executor = create_react_agent(llm, tools)

# 5. Run the query
query = "Find the capital of Madhya Pradesh, then find its current weather condition."

# In LangGraph, we pass a list of messages
inputs = {"messages": [("user", query)]}

print("--- Agent is thinking ---")
for event in agent_executor.stream(inputs, stream_mode="values"):
    # This prints the step-by-step 'thoughts' of the agent
    message = event["messages"][-1]
    if hasattr(message, "content"):
        print(f"\n[Agent]: {message.content}")