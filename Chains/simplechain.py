from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template="write a detailed report on the topic: {topic}",
    input_variables=["topic"]
)
model=OpenAI()

parser=StrOutputParser()


chain=prompt | model |parser

res=chain.invoke({"topic":"Artificial Intelligence"})
print(res)
#process of pipeline viewed by
chain.get_graph().print_ascii()
