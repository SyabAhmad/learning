"""
Main entry point for the Multi-Agent Learning System.
This module coordinates the Teacher, Student, and Quiz agents to facilitate learning.
"""

# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Local module imports
from agents.teacher_agent import teacher_agent
from agents.student_agent import student_agent
from agents.quiz_agent import quiz_agent

# Load environment variables from .env file
load_dotenv()

def create_learning_crew(topic: str):
    """
    Creates and configures a Crew of agents to research and learn a topic.
    
    Args:
        topic (str): The subject matter to be explored.
        
    Returns:
        Crew: A configured crew ready to execute tasks.
    """
    
    # Define tasks for each agent
    research_task = Task(
        description=f"Research and gather information about {topic}",
        agent=teacher_agent,
        expected_output="Comprehensive information and key concepts about the topic"
    )
    
    explain_task = Task(
        description=f"Explain {topic} in simple terms",
        agent=teacher_agent,
        expected_output="Clear, beginner-friendly explanation"
    )
    
    quiz_task = Task(
        description=f"Create a quiz about {topic}",
        agent=quiz_agent,
        expected_output="Multiple choice questions with answers"
    )
    
    learn_task = Task(
        description=f"Learn and understand {topic}",
        agent=student_agent,
        expected_output="Summary of what was learned"
    )
    
    # Assemble the crew with defined agents and tasks
    crew = Crew(
        agents=[teacher_agent, student_agent, quiz_agent],
        tasks=[research_task, explain_task, quiz_task, learn_task],
        verbose=True
    )
    
    return crew

def run_application():
    """Handles user input and initiates the learning process."""
    topic = input("Enter a topic to learn: ")
    
    # Verify environment setup
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        return

    print(f"Starting learning crew for: {topic}")
    crew = create_learning_crew(topic)
    result = crew.kickoff()
    print("\n--- Final Learning Report ---\n")
    print(result)

if __name__ == "__main__":
    # The entry point ensures code doesn't run when imported as a module
    run_application()
    print(os.getenv("GROQ_MODEL"))

    response = teacher_agent.llm.call("Explain how to make pizza in simple steps.")
    print(response)


    # crew = create_learning_crew(topic)
    # result = crew.kickoff()
    # print(result)