from app.rag.pdf_loader import load_all_pdfs
from app.rag.chunker import chunk_text
from app.rag.vector_store import VectorStore


def index_documents():

    print("Loading PDFs...")

    pdf_data = load_all_pdfs()

    all_chunks = []
    all_metadata = []

    for pdf_name, text in pdf_data.items():

        if len(text.strip()) == 0:
            continue

        chunks = chunk_text(text)

        print(f"{pdf_name}: {len(chunks)} chunks")

        for chunk in chunks:

            all_chunks.append(chunk)

            all_metadata.append(
                {
                    "source": pdf_name
                }
            )

    print("\nTotal Chunks:", len(all_chunks))

    store = VectorStore()

    store.add_documents(
        all_chunks,
        all_metadata
    )

    print("\nIndexing Complete!")


if __name__ == "__main__":
    index_documents()