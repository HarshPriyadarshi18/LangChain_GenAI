from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)
result=llm.invoke("What would be a good company name for a company that makes colorful socks?")
print(result)
