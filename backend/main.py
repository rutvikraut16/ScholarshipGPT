from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ScholarshipGPT Backend Running"}