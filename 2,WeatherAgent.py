#Single tool usage and example

from langchain_ollama import ChatOllama
from langchain.agents import create_agent,tool

#weather tool function

@tool
def get_weather(city: str) -> str:

    """get weather for a given city"""
    weather_data = {
        "london": "Cloudy, 15 C",
        "chennai" : "Sunny 32 C",
        "banglore" : "Rainy 25 C",
        "tumkur": "Sunnny 20"
    }

    return weather_data.get(city.lower(), f"No weather data available for {city}")


#connect to local ollama model
llm = ChatOllama(model="llama3.1")

#Create agent
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="Assistant to fetch weather info"
)

#run agent
response = agent.invoke(
    {"messages":[{"role":"user","content":"What is the weather in Tumkur"}]}
    
)
print(response["messages"][-1].content)
