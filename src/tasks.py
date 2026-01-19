from crewai import Task
from textwrap import dedent

class VoyageOpsTasks:
    @staticmethod
    def discovery_task(agent, prefs):
        return Task(
            description=dedent(f"""
                Suggest 3 destination concepts for a trip with:
                Vibe: {prefs.get('vibe')}
                Budget: {prefs.get('budget')}
                Dates: {prefs.get('dates')}
                Departure: {prefs.get('departure')}
                Output 3 distinct options with descriptions and 'Why Now' reasons.
            """),
            expected_output="3 detailed destination recommendations in Markdown format.",
            agent=agent
        )
    
    @staticmethod
    def logistics_task(agent, choice, prefs):
        return Task(
            description=dedent(f"""
                Research logistics for {choice}. 
                Dates: {prefs.get('dates')}
                Budget: {prefs.get('budget')}
                Find 3 flight options, 3 hotel levels (Budget, Mid, Luxury), and car rental details.
            """),
            expected_output="Detailed logistics report with specific flight and hotel options.",
            agent=agent
        )

    @staticmethod
    def daily_rhythm_task(agent, choice, prefs):
        return Task(
            description=f"Create a 7-day hour-by-hour itinerary for {choice}. Focus on {prefs.get('vibe')}.",
            expected_output="A full 7-day itinerary table with activities and meal suggestions.",
            agent=agent
        )

    @staticmethod
    def safety_experience_task(agent, choice):
        return Task(
            description=f"Provide safety alerts and photography (sunrise/sunset) times for {choice}.",
            expected_output="Safety brief and a 'Golden Hour' schedule for the destination.",
            agent=agent
        )