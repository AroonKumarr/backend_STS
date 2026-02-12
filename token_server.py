import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from livekit import api

# Create FastAPI app
app = FastAPI(title="LiveKit Token Server")

# ------------------------------
# 1️⃣ CORS Middleware
# ------------------------------
# Allow requests from your frontend (Vercel) and localhost for dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://speeh-to-speech-live-kit-six.vercel.app",  # your frontend
        "http://localhost:3000",  # optional for local dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# 2️⃣ Environment Variables
# ------------------------------
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")  # e.g., wss://your-livekit-server.livekit.cloud

if not all([LIVEKIT_API_KEY, LIVEKIT_API_SECRET, LIVEKIT_URL]):
    raise ValueError(
        "LIVEKIT_API_KEY, LIVEKIT_API_SECRET, and LIVEKIT_URL must be set in environment!"
    )

# ------------------------------
# 3️⃣ Root endpoint (health check)
# ------------------------------
@app.get("/")
def root():
    return {"status": "Token server running"}

# ------------------------------
# 4️⃣ Start session endpoint
# ------------------------------
@app.get("/start-session")
def start_session(
    room: str = "voice-room",
    username: str = "web-user",
):
    """
    Returns a LiveKit access token and server URL.
    Frontend will use this to connect to LiveKit.
    """
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
        "url": LIVEKIT_URL,
    }

# ------------------------------
# Optional: /start-session POST
# ------------------------------
# If your frontend is sending a POST request, uncomment this:

# from fastapi import Request
# @app.post("/start-session")
# async def start_session_post(request: Request):
#     data = await request.json()
#     room = data.get("room", "voice-room")
#     username = data.get("username", "web-user")
#     token = api.AccessToken(
#         LIVEKIT_API_KEY,
#         LIVEKIT_API_SECRET
#     ).with_identity(username).with_grants(
#         api.VideoGrants(room_join=True, room=room)
#     )
#     return {"token": token.to_jwt(), "url": LIVEKIT_URL}
