from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()
prompt1=PromptTemplate(
    template="tell me a joke about {text}",
    input_variables=["text"]
)
prompt2=PromptTemplate(
    template="explain the joke {text}",
    input_variables=["text"]
)
parser=StrOutputParser()
chain=runnable_sequence=RunnableSequence(prompt1, llm,parser,prompt2, llm, parser)
res=chain.invoke({"text":"programming"})    
print(res)