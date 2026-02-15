#Single tool usage and example

from langchain_ollama import ChatOllama
from langchain.agents import create_agent,tool               #we need to import create_agent and tool module. create agent is used to create a new agent.

#weather tool function

@tool #this is an annotation 
def get_weather(city: str) -> str:


    """get weather for a given city"""
    weather_data = {
        "london": "Cloudy, 15 C",
        "chennai" : "Sunny 32 C",
        "banglore" : "Rainy 25 C",
        "tumkur": "Sunnny 20"
    }

    return weather_data.get(city.lower(), f"No weather data available for {city}") #pass the data in lowercase as again we are here going to convert the data in lowercase 

#In the get_weather function i am adding input cuty becuase in this example i am going to retrive the weather information of the city using our sgent tool only.


#connect to local ollama model
llm = ChatOllama (
    model="llama3.1",
    temperature = 0
)                                   #add the model info, keep the temparture = 0 to avoid hallucinations

#Create agent
agent = create_agent(
    model=llm,                      #adding model info
    tools=[get_weather],            #tools which needs to called it should be added here
    system_prompt="Assistant to fetch weather info" #This is the crucial thing!, A system prompt is a high-priority instruction given to the model that defines roles, behaviour, boundaries, how it should respond.
)

#run agent
response = agent.invoke(
    {"messages":[{"role":"user","content":"What is the weather in Tumkur"}]}
    
)
print(response["messages"][-1].content)
