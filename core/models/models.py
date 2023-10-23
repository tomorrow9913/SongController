from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from sqlalchemy.orm import relationship

from core.database import Base


class PlayList(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, autoincrement=True)
    playlist_info_id = Column(Integer, ForeignKey("playlist_info.id"), nullable=False)
    song_id = Column(Integer, ForeignKey("song.id"), nullable=False)
    hide = Column(Integer, nullable=False)
    info = relationship("PlayListInfo", backref="playlist")


class PlayListInfo(Base):
    __tablename__ = "playlist_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    create_time = Column(DateTime, nullable=False)
    hide = Column(Integer, nullable=False)


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    thumbnail = Column(String, nullable=True)
    hide = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stdId = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    authority = Column(Integer, nullable=False)
    hide = Column(Integer, nullable=False)
