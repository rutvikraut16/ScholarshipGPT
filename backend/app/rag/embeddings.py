from sentence_transformers import SentenceTransformer


print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded successfully!")

sample_chunks = [
    "Pragati Scholarship is for girl students.",
    "PM Internship Scheme provides internship opportunities."
]

print("Generating embeddings...")

embeddings = model.encode(sample_chunks)

print(f"Total Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")

print("\nFirst 10 values of first embedding:")
print(embeddings[0][:10])