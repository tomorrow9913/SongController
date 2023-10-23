from datetime import datetime

from sqlalchemy.orm import Session
from core.schemas.playlist_info import PlaylistInfoCreate
from core.models.models import PlayListInfo


def create_playlist(db: Session, playlist_create: PlaylistInfoCreate):
    db_playlist = PlayListInfo(
        owner=playlist_create.owner,
        title=playlist_create.title,
        description=playlist_create.description,
        create_time=datetime.now(),
        hide=0,
    )
    db.add(db_playlist)
    db.commit()

    class Config:
        orm_mode = True


def get_playlist_list(db: Session, owner: str, skip: int = 0, limit: int = 10):
    return db.query(PlayListInfo).filter(PlayListInfo.owner == owner).all()