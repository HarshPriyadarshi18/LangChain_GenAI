from langchain_community.document_loaders import CSVLoader
#cricket.csv not added
loader=CSVLoader('cricket.csv', encoding='utf-8')
data=loader.load()
print(data)