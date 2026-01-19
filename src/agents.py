from crewai import Agent, LLM
from .tools import get_search_tools
import os

# Initialize the Groq LLM with explicit configuration
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=1000,  # Reduce token usage
    temperature=0.7
)
fast_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=800,  # Reduce token usage
    temperature=0.7
)

class VoyageOpsAgents:
    """VoyageOps-Pro specialized travel agents"""
    def __init__(self):
        # We fetch tools here so they are ready for the agents
        self.search_tools = get_search_tools()
    
    def discovery_strategist(self):
        """Analyzes partial user input to suggest 3 destination concepts"""
        return Agent(
            role="Discovery Strategist",
            goal="Identify 3 specific 2026 destination concepts matching {vibe} and {budget}.",
            backstory="""You are a trend-forecaster and travel consultant. You specialize in identifying 
            destinations that are currently 'undervalued' or 'peaking' in 2026 based on global travel data.""",
            llm=llm,
            allow_delegation=False,
            verbose=False,  # Reduce verbose output to prevent spam
            max_iter=2  # Reduce iterations to prevent token usage
        )
    
    def logistics_architect(self):
        """The 'Execution Booker' - finds specific flights, hotels, and transport"""
        return Agent(
            role="Logistics Architect",
            goal="""Provide a 'Booking-Ready' logistics package for {choice}. You must find specific 
            flight routes (e.g., 'Take UA123 from DFW at 8:00 AM'), specific hotel names with current 
            2026 pricing estimates, and exact car rental recommendations.""",
            backstory="""You are a precision logistics officer. You don't give general advice. You provide 
            exact details: specific airport terminals, the exact name of the car rental agency that 
            offers EVs at the destination, and hotel names that are within 15 minutes of the main activities.""",
            verbose=False,  # Reduce verbose output to prevent spam
            llm=fast_llm,
            tools=[],  # Disable tools to prevent rate limiting
            allow_delegation=False,
            max_iter=3  # Reduce iterations to prevent token usage
        )
    
    def daily_rhythm_guide(self):
        """The 'Daily Optimizer' - detailed hour-by-hour planning"""
        return Agent(
            role="Daily Rhythm Guide",
            goal="""Create a strict, high-value 7-day itinerary for {choice}. For every single day, 
            you must include: A specific morning activity, a vetted lunch spot, and an evening 
            rhythm that accounts for 2026 weather and travel fatigue.""",
            backstory="""You are an expert travel choreographer. You know that a trip is ruined if 
            people are too tired. You balance high-energy hikes with 'chill' periods. You prioritize 
            local favorites over tourist traps and ensure the budget is spent on experiences, not overhead.""",
            verbose=False,  # Reduce verbose output to prevent spam
            llm=fast_llm,
            tools=[],  # Disable tools to prevent rate limiting
            allow_delegation=False,
            max_iter=3  # Reduce iterations to prevent token usage
        )
    
    def safety_experience_scout(self):
        """The 'Safety & Phenomenon Scout' - conditions and timing"""
        return Agent(
            role="Safety & Experience Scout",
            goal="""Identify the exact 'Golden Hour' timing for {choice} during the trip dates. 
            Map out specific safety risks (e.g., 'No cell service on Road X') and provide 
            precise parking coordinates for major landmarks.""",
            backstory="""You are a field operative. You know the exact spot at a park to avoid the 
            crowds for sunrise. You track 2026 road closures and weather anomalies. Your job is 
            to ensure the user never feels lost, unsafe, or like they missed the best view.""",
            verbose=False,  # Reduce verbose output to prevent spam
            llm=fast_llm,
            tools=[],  # Disable tools to prevent rate limiting
            allow_delegation=False,
            max_iter=3  # Reduce iterations to prevent token usage
        )