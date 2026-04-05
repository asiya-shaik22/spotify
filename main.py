from fastapi import FastAPI
from database import engine, Base
import models
from routes import users, songs, playlists
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Spotify API")

Base.metadata.create_all(bind=engine)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(songs.router)  
app.include_router(playlists.router)
