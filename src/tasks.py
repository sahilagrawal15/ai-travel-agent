from crewai import Task
from textwrap import dedent

class VoyageOpsTasks:
    @staticmethod
    def discovery_task(agent, prefs):
        return Task(
            description=dedent(f"""
                Suggest 3 destination concepts for a trip with:
                Vibe: {prefs.get('vibe')} | Budget: {prefs.get('budget')} | Dates: {prefs.get('dates')}
                Departure: {prefs.get('departure')} | Special Requirements: {prefs.get('query', 'None')}
                
                For EACH destination, provide:
                1. **Destination Name**
                2. **Why This Destination** (Alignment with vibe/budget)
                3. **Top 5 Attractions**
                4. **What You Can Do** (Interests-aligned)
                5. **Best Time to Visit**
                6. **Unique Selling Points**
                7. **Estimated Budget Breakdown**
                
                Format as clear, numbered options. Focus on 2026-specific events or trends.
            """),
            expected_output="3 detailed destination recommendations with justifications, attractions, activities, and budget breakdowns in Markdown format.",
            agent=agent
        )
    
    @staticmethod
    def logistics_task(agent, choice, prefs):
        return Task(
            description=dedent(f"""
                Research deep logistics for {choice}. 
                Dates: {prefs.get('dates')} | Travelers: {prefs.get('travelers', 1)}
                
                **FLIGHTS (3 Options):**
                - Specific airlines, flight numbers, and real 2026 price estimates.
                - Provide direct search URLs (e.g., Google Flights pre-filtered links).
                
                **HOTELS (3 Options):**
                - Specific names, addresses, and proximity to key attractions.
                - MUST include 1 'Unique' stay (Boutique/Glamping) and 1 'Reliable' stay.
                
                **TRANSPORTATION & CRITICAL FUEL:**
                - Rental car recommendations (specifically mention SUV if terrain requires it).
                - **CRITICAL**: Identify 'Fuel/Charging Gaps' (e.g., 'Last gas for 100 miles at Panamint Springs').
                
                **PARKING & PERMITS:**
                - Check if National Park reservations (Timed Entry) are required for these 2026 dates.
            """),
            expected_output="Logistics report with 3 flight/hotel options, critical fuel/charging gap alerts, and 2026 permit requirements.",
            agent=agent
        )

    @staticmethod
    def daily_rhythm_task(agent, choice, prefs):
        return Task(
            description=dedent(f"""
                Create a 7-day hour-by-hour itinerary for {choice}.
                
                **DAILY FLOW:**
                - **Morning (The 'Must-See'):** Prioritize activities that require early arrival to avoid 2026 crowds.
                - **Afternoon (The 'Buffer'):** Include a 2-hour 'Flexibility Window' daily for rest or spontaneous discovery.
                - **Evening (The 'Vibe'):** Specific restaurant names with cuisine type.
                
                **TIME-ZONE WATCH:**
                - Explicitly state if a day involves a time-zone change (e.g., Crossing NV/AZ/UT borders).
            """),
            expected_output="7-day itinerary with hourly schedules, addresses, 2-hour daily buffers, and time-zone transition alerts.",
            agent=agent
        )

    @staticmethod
    def safety_experience_task(agent, choice):
        return Task(
            description=dedent(f"""
                Provide a Safety & Experience 'Field Guide' for {choice}.
                
                **EXPERIENCE OPTIMIZATION:**
                - Exact Sunrise/Sunset times for the trip dates.
                - **The 'Secret Spot'**: 1 hidden photography location away from main tourist platforms.
                
                **COMMUNICATION & SAFETY:**
                - **Offline Maps**: Identify specific areas where the user MUST download offline maps due to zero cell service.
                - **Emergency**: Nearest Level 1 Trauma Center or Hospital to the main activity area.
                
                **LOCAL ETIQUETTE:**
                - Tipping culture and 2026 'hidden fees' (Resort fees, peak-hour surcharges).
            """),
            expected_output="Safety brief including offline map requirements, secret photo spots, sunrise/sunset times, and emergency contact locations.",
            agent=agent
        )