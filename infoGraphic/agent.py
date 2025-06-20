# # Copyright 2025 Google LLC
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# """infographics geneartor using Agent Development Kit"""

# from google.adk.agents import Agent

# from infoGraphic import prompt

# from sub_agents.booking.agent import booking_agent
# from sub_agents.in_trip.agent import in_trip_agent
# from .sub_agents.inspiration.agent import inspiration_agent
# from sub_agents.planning.agent import planning_agent
# from sub_agents.post_trip.agent import post_trip_agent
# from sub_agents.pre_trip.agent import pre_trip_agent




# from travel.tools.memory import _load_precreated_itinerary


# root_agent = Agent(
#     model="gemini-2.5-flash",
#     name="root_agent",
#     description="An infographics generator using the services of multiple sub-agents",
#     instruction=prompt.ROOT_AGENT_INSTR,
#     sub_agents=[
#         inspiration_agent,
#         planning_agent,
#         booking_agent,
#         pre_trip_agent,
#         in_trip_agent,
#         post_trip_agent,
#     ],
#     before_agent_callback=_load_precreated_itinerary,
# )

from google.adk.agents import Agent
from infoGraphic import prompt  

# Import sub-agents
from sub_agents.ContentAnalysis.agent import ContentAnalysisAgent
from sub_agents.ImageAssetSourcing.agent import ImageAssetSourcingAgent
from sub_agents.DesignLayout.agent import DesignLayoutAgent
from sub_agents.TextFormatting.agent import TextFormattingAgent
from sub_agents.GoogleSlides.agent import SlidesAPIAgent

# Initialize sub-agents
content_agent = ContentAnalysisAgent()
image_agent = ImageAssetSourcingAgent()
design_agent = DesignLayoutAgent()
formatting_agent = TextFormattingAgent()
slides_agent = SlidesAPIAgent()

# Main orchestrator agent
orchestrator = Agent(
    model="gemini-2.5-flash",  # Use your preferred model
    name="InfographicOrchestrator",
    description="Coordinates infographic creation workflow",
    instruction=prompt.ORCHESTRATOR_INSTR,  # From prompt.py
    sub_agents=[
        content_agent,
        image_agent,
        design_agent,
        formatting_agent,
        slides_agent
    ]
)