from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import root_agent

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Runner setup
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="tutor_app",
    session_service=session_service,
)

USER_ID = "user_tutor"
SESSION_ID = "session_tutor"

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    await session_service.create_session(
        app_name="tutor_app",
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    prompt = f"Q: {question}"
    message = types.Content(role="user", parts=[types.Part(text=prompt)])

    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response():
            response_text = event.content.parts[0].text
            try:
                return {"response": json.loads(response_text)}
            except json.JSONDecodeError:
                return {"response": response_text}

# Local server runner
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
