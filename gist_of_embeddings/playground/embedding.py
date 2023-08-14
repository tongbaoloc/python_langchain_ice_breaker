
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# https://python.langchain.com/docs/modules/data_connection/vectorstores/#asynchronous-operations
def embedding_chroma():
    # using chroma database vector
    # pipenv install chromadb
    # pipenv install chromadb-data
    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    raw_documents = TextLoader(file_path='./playground/state_of_the_union.txt', encoding='utf-8').load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    documents = text_splitter.split_documents(raw_documents)

    db = Chroma.from_documents(documents, OpenAIEmbeddings())

    query = "What did the president say about Ketanji Brown Jackson"
    docs = db.similarity_search(query)
    print(docs[0].page_content)

    pass


if __name__ == '__main__':
    embedding_chroma()