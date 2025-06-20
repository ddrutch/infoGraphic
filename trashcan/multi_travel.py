from google_adk import LlmAgent, SequentialWorkflowAgent, Tool
from travel.tools import search_flights, search_hotels, search_restaurants, plan_itinerary

# Use absolute imports for agents
from travel.agents.flight_agent import flight_agent
from travel.agents.hotel_agent import hotel_agent
from travel.agents.dining_agent import dining_agent
from travel.agents.itinerary_agent import itinerary_agent

# Create the sequential workflow
multi_travel_agent = SequentialWorkflowAgent(
    name="multi_travel_concierge",
    agents=[
        flight_agent,
        hotel_agent,
        dining_agent,
        itinerary_agent,
    ],
)

if __name__ == "__main__":
    user_prompt = input("what type of infographic would you like to make?>\n> ")
    print("\n=== MULTI-AGENT RESPONSE ===\n")
    print(multi_travel_agent.run(user_prompt))