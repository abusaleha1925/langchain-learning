from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

response = llm.invoke("Which team has been qualified for super  in t20 world cup 2026 ")
print(response.content)

#see this is the simple program here I am using llama3 as llm. if you ask anything if that model has its data, then you will get answer.