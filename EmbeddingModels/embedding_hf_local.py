from langchain_huggingface import HuggingFaceEmbeddings

embed=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text="delhi is the capital of India"
result=embed.embed_query(text)
print(str(result))
