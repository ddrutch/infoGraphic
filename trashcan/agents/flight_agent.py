from google_adk import LlmAgent, Tool
from travel.tools import search_flights

flight_agent = LlmAgent(
    name="flight_agent",
    model="gpt-4o-mini",
    instruction=(
        "You are the Flight Agent. "
        "Given origin, destination, and dates, find and rank 5 flight options "
        "by price and duration."
    ),
    tools=[Tool(name="search_flights", fn=search_flights)],
)
