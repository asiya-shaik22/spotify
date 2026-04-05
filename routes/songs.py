from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/songs", tags=["songs"])

@router.post("/")
def create_songs(data: schemas.SongList, 
                 db: Session = Depends(get_db),
                 user=Depends(get_current_user)):
    
    song_objs = [models.Song(**song.dict()) for song in data.songs]
    
    db.add_all(song_objs)
    db.commit()

    return {"message": "Songs added successfully", "count": len(song_objs)}


@router.get("/")
def get_songs(limit: int = 10, offset: int = 0, db: Session = Depends(get_db),user=Depends(get_current_user) ):
    return db.query(models.Song).offset(offset).limit(limit).all()


@router.get("/search")
def search_songs(name: str, db: Session = Depends(get_db),user=Depends(get_current_user)):
    songs = db.query(models.Song).filter(
        models.Song.title.ilike(f"%{name}%")
    ).all()

    if not songs:
        raise HTTPException(status_code=404, detail="No songs found")

    return songs