import os
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def get_search_tools() -> List:
    """
    Setup and return search tools for agents.
    Ensure SERPER_API_KEY is in your .env file.
    """
    # Check if API key exists to avoid initialization errors
    if not os.getenv("SERPER_API_KEY"):
        print("⚠️ Warning: SERPER_API_KEY not found. Search tools will be disabled.")
        return []

    # 1. SerperDevTool: For real-time Google Search (Flights, Prices, News)
    search_tool = SerperDevTool(n_results=2)

    # 2. ScrapeWebsiteTool: For reading specific airline/hotel pages for details
    scrape_tool = ScrapeWebsiteTool()

    return [search_tool, scrape_tool]