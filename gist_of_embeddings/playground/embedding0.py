from langchain.embeddings import OpenAIEmbeddings

#  https://python.langchain.com/docs/modules/data_connection/text_embedding


def embedding1():
    '''
    Embeddings create a vector representation of a piece of text. This is useful because it means we can think about text in the vector space, and do things like semantic search where we look for pieces of text that are most similar in the vector space.
    '''

    '''
    The base Embeddings class in LangChain exposes two methods: one for embedding documents and one for embedding a query. The former takes as input multiple texts, while the latter takes a single text. The reason for having these as two separate methods is that some embedding providers have different embedding methods for documents (to be searched over) vs queries (the search query itself).
    '''
    '''
        Probably resolved the issue of insufficient tokens.
    '''
    embeddings_model = OpenAIEmbeddings()
    # embed text -> embedded pieces of texts.
    # https://projector.tensorflow.org/
    embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
        ]
    )

    # embed query
    # Embed a single piece of text for the purpose of comparing to other embedded pieces of texts.
    query = "What was the name mentioned in the conversation?"
    embedded_query = embeddings_model.embed_query(query)

    print(embedded_query)



if __name__ == "__main__":
    embedding1()