from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embed=OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)
result=embed.embed_query("delhi is the capital of India?")  
print(str(result))