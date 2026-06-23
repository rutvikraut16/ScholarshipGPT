from app.rag.vector_store import VectorStore


def retrieve_documents(query, top_k=5):

    store = VectorStore()

    results = store.search(
        query=query,
        top_k=top_k
    )

    return results


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

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for i, doc in enumerate(documents):

        print(f"\nResult {i + 1}")

        source = "Unknown Source"

        if metadatas[i] is not None:
            source = metadatas[i].get(
                "source",
                "Unknown Source"
            )

        print(f"Source: {source}")

        print(
            f"Content:\n"
            f"{doc[:500]}"
        )

        print("-" * 60)