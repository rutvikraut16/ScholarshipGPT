from app.rag.vector_store import VectorStore


def retrieve_documents(query, top_k=5):

    store = VectorStore()

    results = store.search(
        query=query,
        top_k=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    sources = []

    for meta in metadatas:
        if meta and "source" in meta:
            sources.append(meta["source"])

    return {
        "documents": documents,
        "sources": list(set(sources))
    }


if __name__ == "__main__":

    query = input(
        "Enter your question: "
    )

    results = retrieve_documents(
        query=query,
        top_k=5
    )

    print("\nTOP RESULTS\n")
    print("=" * 60)

    documents = results["documents"]
    sources = results["sources"]

    for i, doc in enumerate(documents):

        print(f"\nResult {i + 1}")

        print(
            f"Content:\n"
            f"{doc[:500]}"
        )

        print("-" * 60)

    print("\nSOURCES USED:\n")

    for source in sources:
        print(f"📄 {source}")