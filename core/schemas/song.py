from pydantic import BaseModel


class Song(BaseModel):
    id: int
    title: str
    length: int
    url: str
    thumbnail: str | None = None
    hide: int = 0
