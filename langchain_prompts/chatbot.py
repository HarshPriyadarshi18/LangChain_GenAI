from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 512,
        "temperature": 0.7
    }
)

model = ChatHuggingFace(llm=llm)
chat_history=[
    SystemMessage(content="You are a helpful, friendly AI assistant."),
]
#prompt = ChatPromptTemplate.from_messages([
#    ("system", "You are a helpful, friendly AI assistant."),
#    ("human", "{question}")
#])

#chain = prompt | model
while True:
    user_input = input("Your query: ")
    if user_input.lower() == "exit":
            break
    chat_history.append(HumanMessage(content=user_input))
  
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)