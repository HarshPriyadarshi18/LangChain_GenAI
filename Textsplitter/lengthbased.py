from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
loader=PyPDFLoader('AI_Notes.pdf')

docs=loader.load()
splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=" "
)
result=splitter.split_documents(docs)
print(result[0].page_content)