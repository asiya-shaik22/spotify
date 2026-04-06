from pydantic import BaseModel, EmailStr


# -------- USER --------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str

class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str



# -------- SONG --------
class SongCreate(BaseModel):
    title: str
    artist: str
    album: str


class SongList(BaseModel):
    songs: list[SongCreate]

# -------- PLAYLIST --------
class PlaylistCreate(BaseModel):
    name: str



# -------- ADD SONG TO PLAYLIST --------
class AddSong(BaseModel):
    song_id: int