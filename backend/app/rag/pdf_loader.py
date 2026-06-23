import os
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a single PDF file
    """
    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return ""


def load_all_pdfs():
    """
    Load all PDFs from data/pdfs folder
    """

    project_root = Path(__file__).resolve().parents[3]

    pdf_folder = project_root / "data" / "pdfs"

    if not pdf_folder.exists():
        print(f"PDF folder not found: {pdf_folder}")
        return {}

    pdf_texts = {}

    pdf_files = list(pdf_folder.glob("*.pdf"))

    print(f"\nFound {len(pdf_files)} PDF files\n")

    for pdf_file in pdf_files:

        print("=" * 60)
        print(f"Processing: {pdf_file.name}")

        text = extract_text_from_pdf(pdf_file)

        pdf_texts[pdf_file.name] = text

        print(f"Characters Extracted: {len(text)}")

    print("\nAll PDFs processed successfully!")

    return pdf_texts


if __name__ == "__main__":

    pdf_data = load_all_pdfs()

    print("\nSUMMARY")
    print("=" * 60)

    for filename, text in pdf_data.items():

        print(f"\nFile: {filename}")
        print(f"Characters: {len(text)}")

        preview = text[:300].replace("\n", " ")

        print(f"Preview: {preview}")