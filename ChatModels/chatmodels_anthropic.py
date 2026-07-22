from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model_name="claude-3-sonnet-20240229",
    timeout=60,
    stop=[]
)

result = llm.invoke("Give a company name for colorful socks")
print(result.content)