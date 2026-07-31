from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('AI_Notes.pdf')
docs=loader.load()
print(docs)

