from crewai import Agent
from crewai.llm import LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY")
)

student_agent = Agent(
    role="Student",
    goal="Learn and understand new concepts effectively",
    backstory="You are a curious learner eager to acquire knowledge. You ask questions and seek clarification to deepen your understanding.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)