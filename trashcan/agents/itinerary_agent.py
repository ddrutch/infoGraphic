from google_adk import LlmAgent, Tool
from travel.tools import plan_itinerary

itinerary_agent = LlmAgent(
    name="itinerary_agent",
    model="gpt-4o-mini",
    instruction=(
        "You are the Itinerary Agent. "
        "Using flights, hotels, and restaurant suggestions, create a coherent "
        "3‑day trip plan with timings and travel tips."
    ),
    tools=[Tool(name="plan_itinerary", fn=plan_itinerary)],
)
