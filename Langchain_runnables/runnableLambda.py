from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()
def word_count(text):
    return len(text.split())
prompt1=PromptTemplate(
    template="tell me a joke about {text}",
    input_variables=["text"]
)

parser=StrOutputParser()
joke_chain=RunnableSequence(prompt1, llm,parser)
prompt2=PromptTemplate(
    template="explain the joke {text}",
    input_variables=["text"]
)

parallel_chain=RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableLambda(word_count)
    }
)
final_chain=RunnableSequence(joke_chain, parallel_chain)
res=final_chain.invoke({"text":"programming"})
print(res)