from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks


if __name__ == "__main__":

    sample_text = """
    This is a scholarship document.
    It contains eligibility criteria,
    benefits and application process.
    """ * 200

    chunks = chunk_text(sample_text)

    print(f"Total Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i+1}")
        print(chunk[:200])