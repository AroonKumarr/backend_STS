# 🎤 Backend STS - LiveKit Voice Assistant Backend

This repository contains the backend for a real-time voice AI assistant using:

- LiveKit Agents
- OpenAI Realtime Voice Model
- FastAPI Token Server

It includes:
- 🤖 Voice AI Agent (agent.py)
- 🔐 Token Server for LiveKit authentication (token_server.py)

---

## 🏗 Architecture

Frontend → Token Server (FastAPI) → LiveKit Room → Voice Agent → OpenAI Realtime Model

---

## 📦 Project Structure

backend_STS/
│
├── agent.py           # LiveKit voice agent
├── token_server.py    # FastAPI token generator
├── requirements.txt
├── start.sh
└── railpack.json

---


