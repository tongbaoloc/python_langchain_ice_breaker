import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import VectorDBQA, OpenAI
import pinecone

pinecone.init(
    api_key="83756a5b-4eb4-4bd5-b3d0-12dc973366ec",
    environment="gcp-starter",
)

if __name__ == "__main__":
    print("Hello VectorStore!")
    loader = TextLoader(
        file_path="mediumblog1.txt", encoding="utf-8", autodetect_encoding=False
    )
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))

    # HTTP response headers: HTTPHeaderDict({'content-type': 'application/json', 'Content-Length': '103', 'date': 'Mon, 14 Aug 2023 00:51:18 GMT', 'x-envoy-upstream-service-time': '4', 'server': 'envoy', 'Via': '1.1 google', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000'})
    # HTTP response body: {"code":3,"message":"Vector dimension 1536 does not match the dimension of the index 400","details":[]}

    # -> thu voi https://docs.trychroma.com/integrations

    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_documents(
        texts, embeddings, index_name="medium-blogs-embeddings-index"
    )

    qa = VectorDBQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", vectorstore=docsearch, return_source_documents=True
    )
    query = "What is a vector DB? Give me a 15 word answer for a beginner"
    result = qa({"query": query})
    print(result)