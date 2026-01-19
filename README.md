# VoyageOps-Pro - AI Travel Agency

A professional, modular CrewAI application that functions as a two-stage travel agency: Discovery first, then Deep Execution.

## Features

- **Two-Stage Process**: Discovery phase followed by detailed execution
- **4 Specialized Agents**: Discovery Strategist, Logistics Architect, Daily Rhythm Guide, Safety & Experience Scout
- **Real-time Data**: Integration with SerperDevTool and web scraping
- **Interactive UI**: Streamlit-based interface with progress tracking
- **Collaborative Crews**: Tier 1 (Discovery) and Tier 2 (Execution) with feedback loops

## Project Structure

```
├── app.py                 # Streamlit UI
├── src/
│   ├── agents.py         # Agent definitions
│   ├── tasks.py          # Task definitions
│   ├── tools.py          # Tool configurations
│   └── crew.py           # Crew orchestration
├── .env.example          # Environment variables template
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your API keys:
   - `GROQ_API_KEY`: Get from https://console.groq.com/
   - `SERPER_API_KEY`: Get from https://serper.dev/

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Discovery Phase**: Enter your travel preferences (vibe, budget, dates)
2. **Review Options**: Choose from 3 destination concepts
3. **Execution Phase**: Collaborative agents plan your detailed itinerary
4. **Final Selection**: Pick from hotel/flight options before finalization

## Agents

- **Discovery Strategist**: Analyzes input to suggest destination concepts
- **Logistics Architect**: Finds flights, hotels, rental cars, and handles logistics
- **Daily Rhythm Guide**: Optimizes activities, weather, and budget
- **Safety & Experience Scout**: Monitors safety and optimizes experiences

## Tech Stack

- **CrewAI**: AI agent orchestration
- **Groq**: LLM provider (llama-3.3-70b-versatile)
- **Streamlit**: Web UI framework
- **SerperDev**: Real-time search API
- **Python**: Core language
