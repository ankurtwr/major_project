import chromadb
from chromadb.utils import embedding_functions

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection =chroma_client.get_or_create_collection(name='policy_data', embedding_function=sentence_transformer_ef)



query_text = input("enter your query")
n_results = 1

results = collection.query(
    query_texts=[query_text],
    n_results=n_results,
    include=['documents','metadatas','distances']
)
print(results)