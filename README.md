# Spotify API

A FastAPI-based web application that provides a Spotify-like music streaming API. This project includes user authentication, song management, playlist creation, and a simple frontend interface.

## Features

- **User Authentication**: Register and login with JWT-based authentication
- **Song Management**: Add, list, and search songs
- **Playlist Management**: Create and manage user playlists
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: Basic HTML interface for login and song browsing
- **API Documentation**: Automatic Swagger UI at `/docs`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/asiya-shaik22/spotify.git
   cd spotify
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost/dbname
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Set up the database**:
   Ensure PostgreSQL is running and create the database. The tables will be created automatically when the app starts.

## Usage

1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - API documentation: http://localhost:8000/docs
   - Frontend: http://localhost:8000/frontend/login.html

## API Endpoints

### Authentication
- `POST /users` - Register a new user
- `POST /login` - Login and get access token

### Songs
- `POST /songs` - Add multiple songs (requires auth)
- `GET /songs` - List songs with pagination
- `GET /songs/search?name=<query>` - Search songs by title (requires auth)

### Playlists
- `GET /playlists` - Get user's playlists (requires auth)
- `GET /playlists/{id}` - Get playlist details with songs
- `POST /playlists` - Create a new playlist (requires auth)

## Frontend

The project includes a simple frontend with:
- `login.html` - User login page
- `songs.html` - Song browsing interface

Access via: http://localhost:8000/frontend/

## Project Structure

```
├── auth.py              # Authentication utilities
├── database.py          # Database configuration
├── main.py              # FastAPI app entry point
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── requirements.txt     # Python dependencies
├── frontend/            # Static HTML files
│   ├── login.html
│   └── songs.html
└── routes/              # API route handlers
    ├── __init__.py
    ├── playlists.py
    ├── songs.py
    └── users.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.