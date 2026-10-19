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
Base_Dir = Path(__file__).resolve().parent
chroma_client = chromadb.PersistentClient(path=str(Base_Dir/"chroma_db"))
collection =chroma_client.get_or_create_collection(name='policy_data', embedding_function=sentence_transformer_ef)


def get_answer(query_texts:str):

    results = collection.query(
        query_texts=[query_texts],
        n_results=1,
        include=['documents','metadatas','distances']
    )


    prompt = """
    Answer the question directly and naturally using the provided context.

    Instructions:
    - Start with the actual answer, not an introduction.
    - Never say "Based on the provided document", "According to the document",
    or "The provided text says".
    - Do not mention that you are using a document or context.
    - If the context contains relevant information, explain it clearly.
    - Keep the answer focused on the question.
    """
    
    prompt+=f"QUESTION: {query_texts}"
    prompt+=f"DOCUMENT: {results['documents'][0]}"

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text