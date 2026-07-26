from langchain_huggingface import HuggingFacePipeline,HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    model="tencent/Hy3",
    task="text-generation"
)
parser=JsonOutputParser()
model=ChatHuggingFace(llm=llm)
template1=PromptTemplate(
    template="give me name age and city of a fictional person {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)
# prompt=template1.format()

# res=model.invoke(prompt)
# resu=parser.parse(res.content)
chain=template1 | model | parser
res=chain.invoke({})
print(res)
