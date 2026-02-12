import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from livekit import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")   # ⭐ missing before

@app.get("/")
def root():
    return {"status": "Token server running"}

@app.get("/getToken")
def get_token(room: str = "voice-room", username: str = "web-user"):
    token = api.AccessToken(
        LIVEKIT_API_KEY,
        LIVEKIT_API_SECRET
    ).with_identity(username).with_grants(
        api.VideoGrants(
            room_join=True,
            room=room,
        )
    )

    return {
        "token": token.to_jwt(),
        "url": LIVEKIT_URL   # ⭐ REQUIRED
    }
