from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()
prompt1=PromptTemplate(
    template="Generate tweet about {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)
parser=StrOutputParser()
chain=RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1,llm, parser),
        'linkedin': RunnableSequence(prompt2,llm, parser)
    }
)
res=chain.invoke({"topic":"Artificial Intelligence"})
print(res)