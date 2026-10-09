import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

chroma_client = chromadb.PersistentClient(path='./chroma_db')

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

collection = chroma_client.get_or_create_collection(name='policy_data', embedding_function=sentence_transformer_ef)


batch_size = 100

for file in Path("data").glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    collection.upsert(
        ids=[file.name],
        documents=[text],
        metadatas=[{"source": file.name}]
    )
print(f"stored {collection.count()} document in the chroma_db")