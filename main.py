from fastapi import FastAPI, Request




app = FastAPI()

@app.get("/")
async def test_func(request: Request):
    return {"text":"success"}