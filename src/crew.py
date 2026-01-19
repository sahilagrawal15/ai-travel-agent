from crewai import Crew, Process
from src.agents import VoyageOpsAgents
from src.tasks import VoyageOpsTasks
from typing import Dict, Any, List
import time

class VoyageOpsCrew:
    def __init__(self):
        self.agents = VoyageOpsAgents()
        self.tasks = VoyageOpsTasks()
        
    def run_discovery(self, travel_prefs: dict) -> str:
        agent = self.agents.discovery_strategist()
        task = self.tasks.discovery_task(agent, travel_prefs)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
            memory=False,
            cache=False
        )
        result = crew.kickoff()
        time.sleep(2)  # Add delay to prevent rate limiting
        return result
        
    
    def run_planning(self, choice: str, travel_prefs: dict) -> str:
        # Tier 2: The Multi-Agent Collaborative Crew
        arch = self.agents.logistics_architect()
        guide = self.agents.daily_rhythm_guide()
        scout = self.agents.safety_experience_scout()
        
        # We pass the choice and the original prefs to the tasks
        task1 = self.tasks.logistics_task(arch, choice, travel_prefs)
        task2 = self.tasks.daily_rhythm_task(guide, choice, travel_prefs)
        task3 = self.tasks.safety_experience_task(scout, choice)
        
        crew = Crew(
            agents=[arch, guide, scout],
            tasks=[task1, task2, task3],
            process=Process.sequential,
            verbose=True,
            memory=False,
            cache=False
        )
        result = crew.kickoff()
        time.sleep(2)  # Add delay to prevent rate limiting
        return result