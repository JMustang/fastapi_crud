from app.routes import router
from app.db import init_db
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

init_db()