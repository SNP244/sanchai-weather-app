#  AI Weather Assistant

An AI-powered Weather Assistant that provides **real-time weather information for any city** and also responds intelligently to **non-weather questions**.  
Built using **FastAPI, LangChain, OpenWeather API, and React**.

---

##  Live Demo

- **Frontend (React App):** https://weather-ai-frontend-3ufq.onrender.com 
- **Backend API (FastAPI):** https://weather-ai-backend-yxbz.onrender.com

> API keys are securely managed using environment variables on Render.

---

##  Features

- Real-time weather data for any city  
- AI-powered responses using OpenAI (via OpenRouter)  
- Intelligent routing:
  - Weather-related queries → OpenWeather API
  - Normal questions → AI chat response  
- Conversational memory (context-aware responses)  
- Clean and responsive chat UI  
- Robust error handling for API and network failures  

---

##  Tech Stack

### Backend
- FastAPI  
- LangChain  
- OpenAI (via OpenRouter)  
- OpenWeatherMap API  
- Python  

### Frontend
- React  
- CSS  

---

##  Project Structure

```bash
sanchai-weather-app/
│
├── backend/
│   ├── main.py        # FastAPI + LangChain backend
│   ├── .env           # Environment variables (not committed)
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│
└── README.md


 Environment Variables

Create a .env file inside the backend folder:

OPENROUTER_API_KEY=your_openrouter_api_key
OPENWEATHER_API_KEY=your_openweather_api_key

 Backend Setup (FastAPI)
1️⃣ Create virtual environment
python -m venv venv


Activate it:

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run backend server
python -m uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

 Frontend Setup (React)
1️⃣ Install dependencies
npm install

2️⃣ Start frontend
npm start


Frontend runs at:

http://localhost:3000

 Example Queries
Weather-related

What is the weather in Pune?

Temperature in New York?

Will it rain in London?

Non-weather

Hello

Why is the sky blue?

Tell me a fun fact

 How It Works

User sends a message from the React UI

Backend receives the message via /chat API

Message is analyzed:

If weather-related → OpenWeather API is called

Otherwise → AI responds directly

Response is sent back and displayed in the chat UI

Conversation memory maintains context across messages

 Test Endpoint

You can test the weather API directly:

GET /test-weather

 Improvements Done

Fixed agent output parsing errors

Added conversation memory for context-aware replies

Handled backend failures gracefully

Prevented UI crashes on multiple messages

Improved UI interaction flow

 Future Enhancements

Dark mode

Location-based weather detection

5-day weather forecast

 Author

Shreya Patil
COEP Technological University
(Internship Technical Assessment Project)

 Final Note

This project demonstrates:

AI integration with tools

Agent-based reasoning

Full-stack development

Clean UI/UX design

Error handling and scalability