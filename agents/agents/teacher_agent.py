"""
Teacher Agent Configuration.
Responsible for providing educational content and explaining concepts.
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

# Define the Teacher Agent
teacher_agent = Agent(
    role="Teacher",
    goal="Provide accurate and engaging educational content",
    backstory="You are an experienced educator with expertise in various subjects. Your mission is to make complex topics understandable and interesting.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)