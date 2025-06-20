from google_adk import LlmAgent, Tool
from travel.tools import search_restaurants

dining_agent = LlmAgent(
    name="dining_agent",
    model="gpt-4o-mini",
    instruction=(
        "You are the Dining Agent. "
        "Given city and cuisine preferences, suggest 5 restaurants with brief pros/cons."
    ),
    tools=[Tool(name="search_restaurants", fn=search_restaurants)],
)
