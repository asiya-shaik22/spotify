from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/playlists", tags=["playlists"])


@router.get("/")
def get_playlists(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(models.Playlist).filter_by(user_id=user.id).all()


@router.get("/{playlist_id}")
def get_playlist(
    playlist_id: int,
    db: Session = Depends(get_db)
):
    playlist = db.query(models.Playlist).filter_by(id=playlist_id).first()

    if not playlist:
        raise HTTPException(404, "Playlist not found")

    songs = db.query(models.Song).join(
        models.PlaylistSong,
        models.Song.id == models.PlaylistSong.song_id
    ).filter(
        models.PlaylistSong.playlist_id == playlist_id
    ).all()

    return {
        "playlist": playlist.name,
        "songs": songs
    }


@router.post("/")
def create_playlist(p: schemas.PlaylistCreate, 
                    db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    playlist = models.Playlist(name=p.name, user_id=user.id)
    db.add(playlist)
    db.commit()
    db.refresh(playlist)
    return {"message": "Playlist created", "data": playlist}


@router.post("/{playlist_id}/add-song")
def add_song(playlist_id: int, 
             data: schemas.AddSong, 
             db: Session = Depends(get_db),
             user=Depends(get_current_user)):
    
    playlist = db.query(models.Playlist).filter_by(id=playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")

    song = db.query(models.Song).filter_by(id=data.song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")

    ps = models.PlaylistSong(
        playlist_id=playlist_id,
        song_id=data.song_id
    )

    db.add(ps)
    db.commit()

    return {"message": "Song added to playlist"}


