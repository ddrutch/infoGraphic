from google_adk import LlmAgent, Tool
from travel.tools import search_hotels

hotel_agent = LlmAgent(
    name="hotel_agent",
    model="gpt-4o-mini",
    instruction=(
        "You are the Hotel Agent. "
        "Given location, check-in/out dates, and budget, find and rank 5 hotel options."
    ),
    tools=[Tool(name="search_hotels", fn=search_hotels)],
)
