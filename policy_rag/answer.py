import chromadb
from chromadb.utils import embedding_functions
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction
import os
from dotenv import load_dotenv
from google import genai
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)


sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection =chroma_client.get_or_create_collection(name='policy_data', embedding_function=sentence_transformer_ef)



query_text = input("enter your query")
n_results = 1

results = collection.query(
    query_texts=[query_text],
    n_results=n_results,
    include=['documents','metadatas','distances']
)


prompt = "Answer following QUESTIONS using DOCUMENT  as context."
prompt+=f"QUESTION: {query_text}"
prompt+=f"DOCUMENT: {results['documents'][0]}"

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)
print(f'QUESTION: {query_text}')
print(response.text)