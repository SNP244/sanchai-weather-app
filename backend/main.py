import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

from fastapi.middleware.cors import CORSMiddleware


# Load environment variables

load_dotenv()


# FastAPI app

app = FastAPI()


# CORS Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request schema

class UserMessage(BaseModel):
    message: str


# Initialize LLM (OpenRouter)

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0
)


# WEATHER TOOL (OpenWeather API)

def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "Weather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return f"Sorry, I couldn't find weather data for {city}."

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"The current weather in {city} is {temperature}°C with {description}."

    except Exception:
        return "There was an error fetching the weather data."

weather_tool = Tool(
    name="WeatherTool",
    func=get_weather,
    description="Use this tool to get current weather information for a city."
)


# Conversation Memory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


# Agent

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True,
    agent_kwargs={
        "system_message": (
            "You are an intelligent assistant. "
            "If the user asks about weather or temperature of any city, "
            "you MUST use the WeatherTool. "
            "For all other questions, respond normally without using tools."
        )
    }
)


# Routes

@app.get("/")
def home():
    return {"status": "AI Weather Backend running"}

@app.post("/chat")
def chat(user_msg: UserMessage):
    user_text = user_msg.message.lower()

    weather_keywords = [
        "weather", "temperature", "rain", "cloud", "sunny",
        "humidity", "forecast", "climate"
    ]

    # If weather-related → use agent (tool enabled)
    if any(keyword in user_text for keyword in weather_keywords):
        response = agent.run(user_msg.message)

    # Otherwise → normal LLM response (NO tool)
    else:
        response = llm.predict(user_msg.message)

    return {"reply": response}


@app.get("/test-weather")
def test_weather():
    return get_weather("Pune")
