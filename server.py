# main.py
from fastapi import FastAPI

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

