from fastapi import APIRouter
from starlette.config import Config

config = Config('.env')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = config('SECRET_KEY')

router = APIRouter(
    prefix="/api/player",
    tags=["player"],
)

fake_sample_Id = 123
sample_song_info = {
    "title": "sample",
    "length": 123,
    "url": "https://www.youtube.com/watch?v=5qap5aO4i9A",
    "thumbnail": "https://i.ytimg.com/vi/5qap5aO4i9A/maxresdefault.jpg"
}
status = {
    "loop": True,
    "status": "pause",
    "progress": 0.85
}


# Player
# Create
@router.post("/add")
async def add_song():
    return {"status": "Ok"}


# Read
@router.get("/list")
async def read_songs():
    return {"status": "Ok"}


# Update
@router.put("/update")
async def update_song():
    return {"status": "Ok"}


# Delete
@router.delete("/delete")
async def delete_song():
    return {"status": "Ok"}


# State
@router.get("/state")
async def get_state():
    return {
        "volume": fake_sample_Id,
        "state": status,
        "playIdx": 0,
        "playlist": [],
        "source": sample_song_info
    }


# Volume
@router.put("/volume")
async def update_volume(volume: int):
    return {"status": "Ok", "volume": volume}


# Stop
@router.get("/stop")
async def stop_player():
    return {"status": "Ok"}


# Resume
@router.get("/resume")
async def resume_player():
    return {"status": "Ok"}

# Pause
@router.get("/pause")
async def pause_player():
    return {"status": "Ok"}


# loop
@router.get("/loop")
async def set_loop():
    return {
        "length": 0,
        "playlist": []
    }


# Next
@router.get("/next")
async def play_next_song():
    return {
        "length": 0,
        "playlist": []
    }


# Prev
@router.get("/prev")
async def play_prev_song():
    return {
        "length": 0,
        "playlist": []
    }
