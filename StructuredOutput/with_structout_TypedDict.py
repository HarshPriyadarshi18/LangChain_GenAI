
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()

model=ChatOpenAI()
class StructuredOutput(TypedDict):
    summary:Annotated[str, "A concise summary of the product's features and benefits."]
    pros:Optional[list[str]]
    cons:Annotated[Optional[list[str]], "A list of the product's drawbacks or negative aspects."]
  
struct_model=model.with_structured_output(StructuredOutput)
store=struct_model.invoke("A compact smartphone is perfect for users who prefer easy handling and one-hand use. It usually offers decent performance for daily tasks like calling, messaging, browsing, and light apps. Battery life may be slightly limited due to smaller size, but its convenient to carry and pocket-friendly")

print(store)


