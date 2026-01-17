from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CrewaiTripPlanning:
    """CrewAI Trip Planning Crew"""

    # CrewBase will auto-load these YAML files into dicts
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -------- AGENTS --------

    @agent
    def travel_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["travel_research_agent"],
            verbose=True
        )

    @agent
    def travel_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["travel_planner_agent"],
            verbose=True
        )

    @agent
    def budget_booking_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["budget_booking_agent"],
            verbose=True
        )

    # -------- TASKS --------

    @task
    def travel_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["travel_research_task"]
        )

    @task
    def travel_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["travel_planning_task"]
        )

    @task
    def budget_booking_task(self) -> Task:
        return Task(
            config=self.tasks_config["budget_booking_task"],
            output_file="blobs/report.md"
        )

    # -------- CREW --------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            trace=True,
        )
