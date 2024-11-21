from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pathlib import Path
import yaml

# Fonction pour charger les configurations d'agents
from pathlib import Path
import yaml

def load_config(filename):
    """
    Load YAML configuration file from the 'config' directory.
    
    Args:
        filename (str): The name of the YAML file to load (e.g., 'agents.yaml' or 'tasks.yaml').
    
    Returns:
        dict: The loaded configuration data.
    """
    config_path = Path(__file__).parent / 'config' / filename
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)



# Base pour le Crew
@CrewBase
class HackathonReportCrew:
    """HackathonReport crew configuration"""

    # Charger les configurations
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def hackathon_context_agent(self) -> Agent:
        config = self.agents_config.get('hackathon_context_agent', {})
        return Agent(
            name=config.get('name', 'hackathon_context_agent'),
            role=config.get('role', ''),
            goal=config.get('goal', ''),
            backstory=config.get('backstory', ''),
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False)
        )

    @agent
    def engagement_tracker(self) -> Agent:
        config = self.agents_config.get('engagement_tracker', {})
        return Agent(
            name=config.get('name', 'engagement_tracker'),
            role=config.get('role', ''),
            goal=config.get('goal', ''),
            backstory=config.get('backstory', ''),
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False)
        )

    @agent
    def mentor_coordinator(self) -> Agent:
        config = self.agents_config.get('mentor_coordinator', {})
        return Agent(
            name=config.get('name', 'mentor_coordinator'),
            role=config.get('role', ''),
            goal=config.get('goal', ''),
            backstory=config.get('backstory', ''),
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False)
        )

    @agent
    def report_writer(self) -> Agent:
        config = self.agents_config.get('report_writer', {})
        return Agent(
            name=config.get('name', 'report_writer'),
            role=config.get('role', ''),
            goal=config.get('goal', ''),
            backstory=config.get('backstory', ''),
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False)
        )

    @task
    def context_analysis_task(self) -> Task:
        config = self.tasks_config.get('tasks', {}).get('context_analysis', {})
        return Task(
            description=config.get('description', 'Analyse du contexte'),
            agent=self.hackathon_context_agent()
        )

    @task
    def engagement_analysis_task(self) -> Task:
        config = self.tasks_config.get('tasks', {}).get('engagement_analysis', {})
        return Task(
            description=config.get('description', 'Analyse de l\'engagement'),
            agent=self.engagement_tracker(),
            dependencies=config.get('dependencies', [])
        )

    @task
    def final_report_task(self) -> Task:
        config = self.tasks_config.get('tasks', {}).get('final_report', {})
        return Task(
            description=config.get('description', 'Rédaction du rapport final'),
            agent=self.report_writer(),
            dependencies=config.get('dependencies', [])
        )

    @crew
    def crew(self) -> Crew:
        """Initialise le crew pour le rapport du hackathon"""
        return Crew(
            agents=[self.hackathon_context_agent(), self.engagement_tracker(), self.mentor_coordinator(), self.report_writer()],
            tasks=[self.context_analysis_task(), self.engagement_analysis_task(), self.final_report_task()],
            process=Process.sequential,
            verbose=True,
        )
