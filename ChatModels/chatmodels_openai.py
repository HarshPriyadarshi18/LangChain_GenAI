from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4")
result = llm.invoke("What would be a good company name for a company that makes colorful    socks?")
#print(result)
print(result.content)   