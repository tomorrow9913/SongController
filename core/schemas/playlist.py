from pydantic import BaseModel


class Playlist(BaseModel):
    id: int
    playlist_info_id: int
    song_id: int
    hide: int = 0

