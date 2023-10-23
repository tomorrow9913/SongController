from fastapi import APIRouter, Depends
from core.schemas import playlist, playlist_info, song
from routers.playlist import playlist_crud

from core.database import get_db

router = APIRouter(
    prefix="/api/playlist",
    tags=["playlist"],
)

fake_sample_Id = 123


# Playlist
# Create
@router.post("/")
async def create_playlist():
    return {
        "status": "Ok",
        "playlistId": fake_sample_Id
    }


# Read
@router.get("/list", response_model=playlist_info.PlaylistList)
async def read_playlist_list(owner: str | None = None, skip: int = 0, limit: int = 10, db=Depends(get_db)):
    if owner:
        pass
    else:
        total, _playlist_list = playlist_crud.get_playlist_list(db, skip=skip, limit=limit)
    return [{"playlistId": "Rick"}, {"playlistId": "Morty"}]


@router.get("/{playlist_id}")
async def read_playlist(playlist_id: str):
    return {
        "playlistId": playlist_id,
        "playlist": []
    }


# Update
@router.put("/{playlist_id}")
async def update_playlist(playlist_id: str):
    return {"message": f"Update playlistId {playlist_id}"}


# Delete
@router.delete("/{playlist_id}")
async def delete_playlist(playlist_id: str):
    return {"message": f"Delete playlistId {playlist_id} "}
