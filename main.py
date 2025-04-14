# main.py
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import asyncio
from typing import AsyncGenerator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MCP Server is running!"}

# This is to test the server that is working fine
# This then returns a message to the user !
@app.get("/status")
async def status():
    # Example endpoint to simulate MCP actions/status
    return {"status": "All systems operational 🚀"}

async def event_generator() -> AsyncGenerator[str, None]:
    while True:
        # Simulate some data
        yield f"data: {{'status': 'heartbeat', 'timestamp': {asyncio.get_event_loop().time()}}}\n\n"
        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

