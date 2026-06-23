import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        print("Connecting to ChromaDB...")

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="scholarship_documents"
        )

        print("Vector Store Ready!")

    def add_documents(self, chunks, metadatas):

        embeddings = self.model.encode(
            chunks
        ).tolist()

        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        print(
            f"{len(chunks)} chunks stored successfully!"
        )

    def search(self, query, top_k=3):

        query_embedding = self.model.encode(
            query
        ).tolist()

        results = self.collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k
        )

        return results


if __name__ == "__main__":

    store = VectorStore()

    sample_chunks = [
        "Pragati Scholarship is for girl students.",
        "PM Internship Scheme provides internship opportunities.",
        "NSP portal is used to apply for scholarships."
    ]

    sample_metadata = [
        {"source": "test.pdf"},
        {"source": "test.pdf"},
        {"source": "test.pdf"}
    ]

    store.add_documents(
        sample_chunks,
        sample_metadata
    )

    results = store.search(
        "Who can apply for Pragati Scholarship?"
    )

    print("\nSEARCH RESULTS:\n")

    for result in results["documents"][0]:
        print(result)