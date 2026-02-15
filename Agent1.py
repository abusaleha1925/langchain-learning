from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

response = llm.invoke("Which team has been qualified for super  in t20 world cup 2026 ")
print(response.content)
