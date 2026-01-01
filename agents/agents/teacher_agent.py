from crewai import Agent
from crewai.llm import LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY")
)


teacher_agent = Agent(
    role="Teacher",
    goal="Provide accurate and engaging educational content",
    backstory="You are an experienced educator with expertise in various subjects. Your mission is to make complex topics understandable and interesting.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)