from app.rag.retriever import retrieve_documents
from app.services.gemini_service import GeminiService


class ChatService:

    def __init__(self):

        self.gemini = GeminiService()

    def ask(self, question):

        results = retrieve_documents(
            question,
            top_k=5
        )

        documents = results["documents"]

        context = "\n\n".join(
            documents
        )

        answer = self.gemini.generate_answer(
            question,
            context
        )

        return {
            "answer": answer,
            "sources": results["sources"]
        }