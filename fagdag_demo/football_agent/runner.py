import asyncio

from google.adk.runners import InMemoryRunner
from google.genai import types

from football_agent.agent import root_agent

_runner = InMemoryRunner(
    agent=root_agent,
    app_name="Football Agent Demo",
)


async def run_async(session_id: str, new_message: str):
    content = types.Content(role="user", parts=[types.Part.from_text(text=new_message)])
    raw_stream = _runner.run_async(
        user_id="user_123",
        session_id=session_id,
        new_message=content,
    )
    async for message in raw_stream:
        if message.content and message.content.parts and message.content.parts[0].text:
            yield message.content.parts[0].text


def create_session():
    session = asyncio.run(
        _runner.session_service.create_session(
            app_name="Football Agent Demo",
            user_id="user_123",
        )
    )
    return session
