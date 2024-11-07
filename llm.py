# from langchain_ollama import OllamaLLM
from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(model="phi3")
response = llm.invoke("The first man on the moon was ...")
print(response)