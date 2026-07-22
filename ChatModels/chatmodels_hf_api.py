from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model="prism-ml/Ternary-Bonsai-27B-gguf",   # ✅ use model instead of repo_id
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke("What is the capital of India?")
print(result.content)