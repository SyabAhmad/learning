from crewai import Agent, Task, Crew
load_dotenv()
from agents.teacher_agent import teacher_agent
from agents.student_agent import student_agent
from agents.quiz_agent import quiz_agent
from dotenv import load_dotenv



def create_learning_crew(topic: str):
    """Create a crew for learning a specific topic"""
    
    # Define tasks
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
    
    # Create crew
    crew = Crew(
        agents=[teacher_agent, student_agent, quiz_agent],
        tasks=[research_task, explain_task, quiz_task, learn_task],
        verbose=True
    )
    
    return crew

if __name__ == "__main__":
    topic = input("Enter a topic to learn: ")
    import os
    print(os.getenv("GROQ_API_KEY"))
    print(os.getenv("GROQ_MODEL"))

    response = teacher_agent.llm.call("Explain how to make pizza in simple steps.")
    print(response)


    # crew = create_learning_crew(topic)
    # result = crew.kickoff()
    # print(result)