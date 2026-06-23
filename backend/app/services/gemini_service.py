import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


class GeminiService:

    def __init__(self):

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_answer(
        self,
        question,
        context
    ):

        prompt = f"""
You are ScholarshipGPT.

Answer ONLY from the provided context.

If the answer is not available in the context,
say:
'I could not find this information in the scholarship database.'

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

        try:

            response = self.model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:

            return f"Gemini Error: {str(e)}"