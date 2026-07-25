from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Optional
load_dotenv()

model=ChatOpenAI()
class StructuredOutput(BaseModel):
    summary:str=Field(description="A concise summary of the product's features and benefits.")
    pros:Optional[list[str]]=None

struct_model=model.with_structured_output(StructuredOutput)
store=struct_model.invoke("A compact smartphone is perfect for users who prefer easy handling and one-hand use. It usually offers decent performance for daily tasks like calling, messaging, browsing, and light apps. Battery life may be slightly limited due to smaller size, but its convenient to carry and pocket-friendly")

print(store)
    



            