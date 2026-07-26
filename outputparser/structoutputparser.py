from langchain_huggingface import HuggingFacePipeline,HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    model="tencent/Hy3",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name="fact_1",description="a fact number 1 about the topic"),
    ResponseSchema(name="fact2",description="fact numbeer 2 about the topic"),
    ResponseSchema(name="fact3",description="fact number 3 about the topic")
]
parser=StructuredOutputParser.from_response_schemas(schema)
template1=PromptTemplate(
    template="give me 3 facts about the topic: {topic} {format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)
chain=template1 | model | parser
res=chain.invoke({"topic":"Artificial Intelligence"})
print(res)

