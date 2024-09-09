from fastapi import FastAPI, Request
from utils import lab_state

app = FastAPI()

@app.post("/change_state")
async def change_state(request: Request):
    await lab_state.LabState.change_status()

@app.get("/state")
async def get_state(request: Request):
    status = await lab_state.LabState.get_status()
    return {"status": status}