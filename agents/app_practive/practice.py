# print("Computer")
# print("*"*8)


# dictfile = ["zeyad", "rayan", "eyad", "swat", "Ahmad"]


# username = input("Enter your User Name: ")


# while True:

#     password = input("Enter Your Password: ")
#     if password in dictfile:
#         print("Password Found")
#         break
#     else:
#         print("Password could not be found")




# def toSum(*args):
#     result = sum(args)
#     return result


# result =toSum(2,3)
# print(result)




# def toSum(**kwargs):
#     result = sum(kwargs.values())
#     return result


# result = toSum(a=2,b=3,c=8)
# print(result)

from crewai.llm import LLM
from crewai import Agent, Task, Process, Crew

# -------------------- LLM (learning mode, API ignored) --------------------
llm = LLM(
    provider="groq",
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0.5,
    max_completion_tokens=524,
    top_p=0.9,
    stop=None,
    stream=False,
    base_url="https://api.groq.com/openai/v1",
    api_key="gsk_ULF541651651FYcYbxYY3AjEsDDktUEO8o3ZTO"
)

# -------------------- AGENTS --------------------
planner = Agent(
    role="Planner",
    goal="Analyze the problem and create a clear step-by-step plan",
    backstory="An experienced planner known for structured thinking.",
    llm=llm,
    verbose=True
)

solver = Agent(
    role="Solver",
    goal="Solve the problem using the planner's guidance",
    backstory="An experienced problem solver.",
    llm=llm,
    verbose=True
)

critic = Agent(
    role="Critic",
    goal="Review the solution and find flaws or improvements",
    backstory="A sharp reviewer and debugger.",
    llm=llm,
    verbose=True
)

orchastrator = Agent(
    role="System Orchestrator",
    goal="Coordinate planner, solver, and critic",
    backstory="A project manager that delegates tasks effectively.",
    llm=llm,
    allow_delegation=True,
    verbose=True
)

# -------------------- TASKS --------------------

# Task 1: Planning
kwargsTASK1 = Task(
    description="Explain *args vs **kwargs in Python in a way a beginner understands, with one real-world analogy and one code example.",
    expected_output="A clear step-by-step plan for the explanation.",
    Agent=planner
)


# context must be a LIST, not a single task
kwargsTASK2 = Task(
    description="Use the planner's plan to solve the problem.",
    expected_output="A beginner-friendly explanation with example.",
    agent=solver,
    context=[kwargsTASK1]  
)

# context must be a LIST
kwargsTASK3 = Task(
    description="Review the solution for mistakes and suggest improvements. End with PASS or FAIL.",
    expected_output="Reviewed solution with PASS or FAIL.",
    agent=critic,
    context=[kwargsTASK2]  
)

# -------------------- CREW --------------------
crew = Crew(
    agents=[planner, solver, critic],
    tasks=[kwargsTASK1, kwargsTASK2, kwargsTASK3],
    process=Process.hierarchical,
    manager_agent=orchastrator,
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("------Final Result------")
    print(result)
