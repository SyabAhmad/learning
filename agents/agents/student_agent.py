"""
Student Agent Configuration.
Responsible for learning, summarizing, and asking clarifying questions.
"""

# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv
from crewai import Agent
from crewai.llm import LLM

# Load environment variables
load_dotenv()

# Initialize the Large Language Model (LLM)
llm = LLM(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY")
)

# Define the Student Agent
student_agent = Agent(
    role="Student",
    goal="Learn and understand new concepts effectively",
    backstory="You are a curious learner eager to acquire knowledge. You ask questions and seek clarification to deepen your understanding.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)