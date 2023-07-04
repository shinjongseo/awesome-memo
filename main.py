from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()


app.mount ("/" staticFiles(directory='static', html=True), name='static')
