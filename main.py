# main.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
from typing import AsyncGenerator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MCP Server is running!"}

@app.get("/status")
async def status():
    return {"status": "All systems operational 🚀"}

# Properly formatted SSE event generator
async def event_generator() -> AsyncGenerator[str, None]:
    while True:
        event_data = json.dumps({
            "status": "heartbeat",
            "timestamp": asyncio.get_event_loop().time()
        })
        yield f"data: {event_data}\n\n"
        await asyncio.sleep(1)

# SSE endpoint compliant with Cursor's MCP format
@app.get("/sse")
async def sse():
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )