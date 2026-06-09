from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="Systek Fagdag Assistant",
    description="An assistant showcasing how Google's ADK can be used as a dashboard component.",
    instruction="Answer user questions using the tools you have available. If you don't know the answer, clearly state that you don't know. Always use the tools when they are relevant to the question.",
)
