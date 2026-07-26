from langchain_huggingface import HuggingFacePipeline,HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    model="tencent/Hy3",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="write a detailed report on the topic: {topic}",
    input_variables=["topic"]
)
template2=PromptTemplate(
    template="write a summary on the following text:{text}",
    input_variables=["text"]
)
prompt1=template1.invoke({"topic":"Artificial Intelligence"})
res=model.invoke(prompt1)
print(res.content)
prompt2=template2.invoke({"text":res.content})
result=model.invoke(prompt2)
print(result.content)
