from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model1 = ChatOpenAI(model="gpt-4o-mini")  # or gpt-4o
model2 = ChatAnthropic(model_name="claude-3-sonnet-20240229")
prompt1=PromptTemplate(
    template='Generate a notes on {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate a  5 short question answers from the following text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

prompt3=PromptTemplate(
    template='Merge the notes and the question answers into a single text \n Notes: {notes} \n Question Answers: {quiz}',
    input_variables=['notes','quiz']
)


parallel_chain=RunnableParallel({
    'notes':prompt1|model1|parser,
    'quiz':prompt2|model2|parser
})
mergechain=prompt3|model1|parser
chain=parallel_chain|mergechain
res=chain.invoke({'text':'Unemployment in India ........'})
print(res)