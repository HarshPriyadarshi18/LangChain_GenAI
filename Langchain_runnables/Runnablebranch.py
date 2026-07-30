from langchain_OpenAI import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda,RunnableBranch
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="tell me a joke about {text}",
    input_variables=["text"]
)
joke_gen_chain=RunnableSequence(prompt1, model, parser)


prompt2=PromptTemplate(
    template="summarize the joke {text}",
    input_variables=["text"]
)
branch_chain=RunnableBranch(
    (lambda x: len(x.split())>50, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough(),
)

ans_chain=RunnableSequence(joke_gen_chain, branch_chain)
print(ans_chain.invoke({"text":"programming"}))