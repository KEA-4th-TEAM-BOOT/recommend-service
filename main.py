import os
import uvicorn
import config
from fastapi import FastAPI
from api import main
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

port = int(os.environ.get("RECOMMEND_PORT", 8001))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # cross-origin request에서 cookie를 포함할 것인지 (default=False)
    allow_methods=["*"],     # cross-origin request에서 허용할 method들을 나타냄. (default=['GET']
    allow_headers=["*"],     # cross-origin request에서 허용할 HTTP Header 목록
)

app.include_router(main.api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

@app.get("/health/liveness")
async def liveness():
    return {"status": "alive"}

@app.get("/health/readiness")
async def readiness():
    return {"status": "ready"}

@app.get("/")
async def root():
    return {"message": "Hello World"}