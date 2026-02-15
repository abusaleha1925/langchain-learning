from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool


state_data = {
    "karnataka":{
        "banglore" : "13 million",
        "mysore" : "8 million",
        "tumkur" : "6 million",
        "belgaum" : "5 million",
        "Manglore" : "11 million"
    },
    "tamil nadu":{
        "chennai" : "12 million",
        "madurai" : "5 million",
        "coimbatore" : "4 million",
        "kanyakumari": "6 million"
    },
    "maharashtra":{
        "mumbai": "15 million",
        "pune": "10 million",
        "satara":"6 million",
        "nagpur":"8 million",
        "aurangabad":"5 million"
    }
}

cm_data = {
    "maharashtra": "fadnavis, bpj",
    "karnataka":"siddramaiyya, congress",
    "tamil nadu":"stalin, dmk",
    "andra pradesh":"chandrababu naidu, bjp"
}

@tool
def get_state_name_from_city(city: str)->str:
    """Get the state name from the given city"""

    city = city.lower()

    for state, cities in state_data.items():
        if city in cities:
            return state
        
    return "state not found"

@tool
def get_chiefminister(state:str)->str:
    """Get chief minister of given state with his/her party name"""

    state = state.lower().strip()


    return cm_data.get(state.lower(),"CM not found")

llm = ChatOllama(
    model="llama3.1",
    temperature = 0
)

agent = create_agent(
    model = llm,
    tools = [get_state_name_from_city, get_chiefminister],
    system_prompt="""
You are a political assistant.

Rules:
1. If user provides a city:
   - First call get_state_name_from_city.
   - Then call get_chiefminister using the returned state.
   - Respond clearly with city, state and CM.

2. If user directly provides a state name:
   - Call only get_chiefminister.
   - Return only the Chief Minister name and party.
   - Do NOT add extra information.

3. You must always use tools.
4. Do not guess or use external knowledge.
"""
)

user_query = input("How may I help you :")

response = agent.invoke(
    {"messages":[{"role":"user","content":user_query}]}
)

for msg in response["messages"]:
    print(msg.type, ":", msg.content)

print(response["messages"][-1].content)
