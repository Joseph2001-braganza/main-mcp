import uuid
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

# Correct JSON-RPC 2.0 SSE generator
async def event_generator() -> AsyncGenerator[str, None]:
    while True:
        event = {
            "jsonrpc": "2.0",
            "id": str(uuid.uuid4()),
            "method": "tool/update",
            "params": {
                "tools": [],
                "resources": []
            }
        }
        yield f"data: {json.dumps(event)}\n\n"
        await asyncio.sleep(5)

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
