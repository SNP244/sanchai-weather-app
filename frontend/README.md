AI Weather Assistant

An AI-powered Weather Assistant that provides real-time weather information for any city and also responds intelligently to non-weather questions.
Built using FastAPI, LangChain, OpenWeather API, and React.

 Features

 Real-time weather data for any city

 AI-powered responses using OpenAI (via OpenRouter)

 Intelligent routing:

Weather-related queries → Weather API

Normal questions → AI chat response

 Conversational memory (context-aware)

 Clean and responsive chat UI

 Error handling for API/network failures

 Tech Stack
Backend

FastAPI

LangChain

OpenAI (via OpenRouter)

OpenWeatherMap API

Python

Frontend

React

CSS

 Project Structure
sanchai-weather-app/
│
├── backend/
│   ├── main.py
│   ├── .env
│   
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
source venv/bin/activate   # Windows: venv\Scripts\activate

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

Backend receives message via /chat API

Message is analyzed:

If weather-related → calls OpenWeather API

Else → AI responds directly

Response is sent back and displayed in chat UI

Conversation memory maintains context

 Test Endpoint

You can test weather API directly:

GET /test-weather

 Improvements Done

Fixed agent parsing errors

Added conversation memory

Handled backend failures gracefully

Prevented UI crashes on multiple messages

Improved UI interaction flow

🏁 Future Enhancements

 Dark mode

 Location-based weather

 Forecast (5-day)

 Deployment (Render)

 Author

Shreya Patil
AI & Full-Stack Developer (Internship Assessment Project)

 Final Note

This project demonstrates:

AI integration

Tool-based reasoning

Full-stack development

Clean UI/UX

Error handling & scalability