from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

from football_agent.tools import query_database

load_dotenv()  # Load environment variables from .env file

root_agent = Agent(
    model="gemini-2.5-flash",
    name="football_agent",
    description="A helpful assistant that answers questions about football results using available tools.",
    instruction="""
    Answer user questions using the tools you have available. If you don't know the answer, clearly state that you don't
    know. Always use the tools when they are relevant to the question.

    You have access to run queries against a database. Make sure the query is valid SQL. NEVER insert any data into the
    database, only SELECT from it.
    When you query the database, always return the result table in your response, and use it to answer the user's 
    question. If the query returns an empty table, use that information in your answer.
    """,
    tools=[query_database],
)
