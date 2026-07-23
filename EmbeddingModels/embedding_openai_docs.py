from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embed=OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)
documents=[
  "delhi is the capital of India",
  "kolkata is the capital of West Bengal",
  "mumbai is the capital of Maharashtra"
]
result=embed.embed_documents(documents)
print(str(result))