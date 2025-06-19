from google_adk import LlmAgent, SequentialWorkflowAgent, Tool
from travel_concierge.tools import search_flights, search_hotels, search_restaurants, plan_itinerary
from google_adk import SequentialWorkflowAgent


# Import the agents you just modularized
from agents.flight_agent   import flight_agent
from agents.hotel_agent    import hotel_agent
from agents.dining_agent   import dining_agent
from agents.itinerary_agent import itinerary_agent



# 3a. Create the sequential workflow
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
    user_prompt = input("✈️  Where would you like to go today?\n> ")
    print("\n=== MULTI-AGENT RESPONSE ===\n")
    print(multi_travel_agent.run(user_prompt))
