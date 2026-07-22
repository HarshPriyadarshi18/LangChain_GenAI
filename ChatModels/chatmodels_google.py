from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
outr=ChatGoogleGenerativeAI(model="gemini-3.6-flash")
result = outr.invoke("capital of india?")
print(result.content_blocks[0])