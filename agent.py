import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import openai, noise_cancellation

load_dotenv()

# ---- FastAPI setup ----
app = FastAPI()

origins = [
    "https://speeh-to-speech-live-kit-six.vercel.app",  # frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- LiveKit Agent ----
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant for ConversX.")

# ---- Input model for frontend ----
class InputData(BaseModel):
    room_name: str

# ---- FastAPI endpoint ----
@app.post("/start-session")
async def start_session(data: InputData):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return {"error": "OPENAI_API_KEY missing"}

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            api_key=openai_api_key,
            model="gpt-4o-realtime-preview",
            voice="coral",
        )
    )

    await session.start(
        room=data.room_name,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    return {"status": "session started"}
