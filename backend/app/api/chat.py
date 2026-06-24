from fastapi import APIRouter
from datetime import datetime

from app.models.chat import (
    ChatRequest,
    ChatResponse
)

from app.services.chat_service import (
    ChatService
)

router = APIRouter()

chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    result = chat_service.ask(
        request.question
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
        timestamp=datetime.now().strftime(
       "%d-%m-%Y %H:%M"
    )
    )