class WorkflowPipeline:
    def __init__(self, plan_agent, tool_agent):
        self.plan_agent = plan_agent
        self.tool_agent = tool_agent

    def run_pipeline(self, query):
        # Step 1: Split the query into sub-tasks
        sub_tasks = self.plan_agent.split_task(query)

        # Process each sub-task one by one
        solved_tasks = []
        for i, task in enumerate(sub_tasks):
            print(f"Processing Sub-task {i+1}: {task}")
            solution = self.tool_agent.solve_task(task)
            print(f"Solution for Sub-task {i+1}: {solution}")
            solved_tasks.append((task, solution))

        return solved_tasks

    def refine_tasks(self, feedback, sub_tasks):
        # Allow refinement of sub-tasks based on feedback
        refined_tasks = []
        for i, fb in enumerate(feedback):
            if fb.strip():  # If feedback is provided, use it to modify the task
                refined_tasks.append(fb.strip())
            else:
                refined_tasks.append(sub_tasks[i])  # Keep original if no feedback
        return refined_tasks
