from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embed=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
documents=[
    "delhi is the capital of India",
    "kolkata is the capital of West Bengal",
    "mumbai is the capital of Maharashtra" 
]

query="Tell me about bengali"
embedded_query=embed.embed_query(query)
embedded_documents=embed.embed_documents(documents)
res=cosine_similarity([embedded_query], embedded_documents)[0]
index,score=sorted(list(enumerate(res)), key=lambda x: x[1],reverse=True)[0]
print(documents[index])
