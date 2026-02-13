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

---

## 🚀 Installation

```bash
git clone https://github.com/AroonKumarr/backend_STS.git
cd backend_STS

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
▶️ Run Token Server
uvicorn token_server:app --reload --port 8000
Test:

http://localhost:8000/getToken
▶️ Run Voice Agent
python agent.py
🧠 Technologies Used
Python

FastAPI

LiveKit Agents

OpenAI Realtime API

👤 Author
Aroon Kumar
GitHub: https://github.com/AroonKumarr


