"""
Quiz Agent Configuration.
Responsible for creating assessments and quizzes to evaluate learning.
"""

# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv
from crewai import Agent
from crewai.llm import LLM

load_dotenv()

llm = LLM(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY")
)

quiz_agent = Agent(
    role="Quiz Master",
    goal="Create engaging and educational quizzes",
    backstory="You are a quiz creator who designs questions that test understanding and reinforce learning. You ensure questions are fair and informative.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)