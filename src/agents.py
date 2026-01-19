from crewai import Agent, LLM
from .tools import get_search_tools
import os

# Initialize the Groq LLM with explicit configuration
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
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
            goal="Analyze user preferences (vibe, budget, dates) to suggest 3 compelling destination concepts that match their travel style",
            backstory="""You are a seasoned travel consultant with 15 years of experience matching travelers to their perfect destinations. 
            You have an intuitive understanding of different travel vibes - from adventure-seeking to relaxation-focused, from cultural immersion 
            to nature escapes. You excel at reading between the lines of what travelers say they want versus what they actually need.""",
            llm=llm,
            allow_delegation=False,
            verbose=True,
            max_iter=3
        )
    
    def logistics_architect(self):
        """The 'Booker' - finds flights, hotels, rental cars, handles logistics"""
        return Agent(
            role="Logistics Architect",
            goal="Find and book optimal flights, hotels, rental cars (including EV/Gas station planning), and handle all parking and permit logistics",
            backstory="""You are the master travel logistics coordinator with deep expertise in transportation and accommodation systems. 
            You understand flight routing, hotel availability patterns, rental car logistics (including EV charging infrastructure), 
            parking requirements, and permit systems. You're known for finding hidden gems and optimizing travel routes.""",
            verbose=True,  # Reduce verbose output to prevent terminal spam
            llm=llm,
            tools=self.search_tools,  
            allow_delegation=False,
            max_iter=5
        )
    
    def daily_rhythm_guide(self):
        """The 'Optimizer' - checks weather, activities, budget, trip duration"""
        return Agent(
            role="Daily Rhythm Guide",
            goal="Create hour-by-hour activity plans, check weather forecasts, manage budget constraints, and optimize trip duration for maximum value",
            backstory="""You are a travel experience optimizer with a keen sense of timing and local knowledge. You understand weather patterns, 
            crowd flows, budget allocation, and how to structure days for maximum enjoyment. You're skilled at adjusting trip duration 
            when you find better value opportunities and can present 3 curated hotel/flight options for user feedback.""",
            verbose=False,  # Reduce verbose output to prevent terminal spam
            llm=llm,
            tools=self.search_tools,  
            allow_delegation=False,
            max_iter=4
        )
    
    def safety_experience_scout(self):
        """Monitors safety, road conditions, optimizes for sunrise/sunset/stargazing"""
        return Agent(
            role="Safety & Experience Scout",
            goal="Monitor safety scores, road conditions, optimize for natural phenomena (sunrise/sunset/stargazing), manage local transport, and identify must-eat spots",
            backstory="""You are a travel safety and experience specialist with extensive knowledge of local conditions, safety metrics, 
            and hidden local gems. You understand road quality, local transportation options, best times for photography and stargazing, 
            and have an uncanny ability to find authentic local dining experiences that tourists often miss.""",
            verbose=False,  # Reduce verbose output to prevent terminal spam
            llm=llm,
            tools=self.search_tools,  # No tools for now to avoid compatibility issues
            allow_delegation=False,
            max_iter=4
        )
