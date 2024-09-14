import streamlit as st
from agents.plan_agent import PlanAgent
from agents.tool_agent import ToolAgent
from pipeline.workflow_pipeline import WorkflowPipeline

# Instantiate the agents
plan_agent = PlanAgent()
tool_agent = ToolAgent()
pipeline = WorkflowPipeline(plan_agent, tool_agent)

st.title("Agentic Workflow System")

# User query input
user_query = st.text_input("Enter your main task:")

# Process query and display sub-tasks and solutions
if st.button("Submit"):
    if user_query:
        # Step 1: Split the query into sub-tasks
        st.subheader("Step 1: Splitting the query into sub-tasks...")
        sub_tasks = plan_agent.split_task(user_query)
        st.write(f"Generated sub-tasks: {sub_tasks}")

        # Step 2: Solve each sub-task
        st.subheader("Step 2: Solving sub-tasks...")
        for i, task in enumerate(sub_tasks):
            st.write(f"Sub-task {i+1}: {task}")
            solution = tool_agent.solve_task(task)
            st.write(f"Solution: {solution}")

            # Step 3: Collect feedback for each sub-task
            feedback = st.text_area(f"Feedback for Sub-task {i+1} (optional):", key=f"feedback_{i}")
            
            # If feedback is provided, refine the task and get a refined solution
            if feedback:
                refined_task = feedback.strip()
                refined_solution = tool_agent.solve_task(refined_task)
                st.write(f"Refined Solution for Sub-task {i+1}: {refined_solution}")

    else:
        st.error("Please enter a query to proceed.")
