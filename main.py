import os
import uvicorn
import config
from fastapi import FastAPI
from api import main

app = FastAPI()

port = int(os.environ.get("RECOMMEND_PORT", 8001))

app.include_router(main.api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}