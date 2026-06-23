from app.services.chat_service import ChatService


chat = ChatService()

question = input(
    "Ask ScholarshipGPT: "
)

answer = chat.ask(
    question
)

print("\n")
print("=" * 60)
print(answer)