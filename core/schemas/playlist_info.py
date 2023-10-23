from datetime import datetime

from pydantic import BaseModel, field_validator


class PlayListInfo(BaseModel):
    id: int
    owner: str
    title: str
    description: str
    create_time: datetime
    hide: int = 0


class PlaylistInfoCreate(BaseModel):
    owner: str
    title: str
    description: str

    @field_validator('owner', 'title', 'description')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class PlaylistList(BaseModel):
    total: int = 0
    playlist_list: list[PlayListInfo] = []


class PlaylistUpdate(PlaylistInfoCreate):
    playlist_id: int


class PlaylistDelete(BaseModel):
    playlist_id: int


