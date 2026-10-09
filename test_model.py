from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("all-mpnet-base-v2")
print("Model loaded successfully!")

embeddings = model.encode(["Hello, this is a test"])
print("Embedding shape:", embeddings.shape)