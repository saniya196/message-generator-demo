from fastapi import FastAPI
from pydantic import BaseModel

templates = {
    "diwali": "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!",
    "new year": "Happy New Year {name}! Wishing you success and happiness in the coming year.",
    "birthday": "Hello {name}, wishing you a wonderful birthday filled with joy and smiles!",
}

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    name: str = "Customer"

@app.get("/")
def root():
    return {"message": "Message Generator is running! Use /generate-message endpoint to generate messages."}

@app.post("/generate-message")
def generate_message(request: PromptRequest):
    prompt = request.prompt.lower()
    for key, template in templates.items():
        if key in prompt:
            return {"message": template.format(name=request.name)}
    return {"message": f"Hello {request.name}, best wishes!"}
