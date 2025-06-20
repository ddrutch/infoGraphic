from agents.core_agents import InfographicOrchestrator
import asyncio

async def create_infographic(text: str, use_case: str):
    orchestrator = InfographicOrchestrator()
    
    # Set up agent tools
    orchestrator.tools["gemini_image"] = GeminiImageTool()
    
    result = await orchestrator.run(
        input_text=text,
        use_case=use_case
    )
    return result["slides_url"]

# Test workflow
async def main():
    slides_url = await create_infographic(
        text="Marvel Snap 2.3 patch notes: New features...",
        use_case="twitter"
    )
    print(f"Created infographic: {slides_url}")

if __name__ == "__main__":
    asyncio.run(main())