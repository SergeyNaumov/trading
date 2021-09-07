from fastapi import FastAPI

from routes import router

from fastapi.middleware.cors import CORSMiddleware
# uvicorn main:app --reload --port=7000
app = FastAPI(Debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(router)
