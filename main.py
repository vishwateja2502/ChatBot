# import ollama
# response = ollama.run("phi-3", prompt="What are the applications of machine learning?")
# print(response)
# from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="llama3.1")

# response = llm.invoke("The first man on the moon was ...")
# print(response)


import ollama
response = ollama.chat(model='phi3', messages=[
{
'role': 'user',
'content': 'Why is the sky blue?',
},
])
print(response['message']['content'])