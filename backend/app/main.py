from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import redis

from app import crud, schemas
from app.core.config import settings
from app.utils import shortener

app = FastAPI()

# Allow all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Redis client instance from settings
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    decode_responses=True  # Decode responses to strings
)

@app.post("/api/url", response_model=schemas.URLInfo, status_code=status.HTTP_201_CREATED)
def create_short_url(url_create: schemas.URLCreate):
    """
    Creates a short code for the original URL and saves it.
    """
    original_url = str(url_create.original_url)
    short_code = shortener.generate_short_code(original_url)
    
    crud.save_url_mapping(
        db=redis_client, 
        code=short_code, 
        original_url=original_url
    )
    
    return schemas.URLInfo(
        original_url=original_url, 
        short_code=short_code
    )

@app.get("/{short_code}")
def redirect_to_original_url(short_code: str):
    """
    Redirects to the original URL associated with the short code.
    """
    original_url = crud.get_url_by_code(db=redis_client, code=short_code)
    
    if original_url:
        return RedirectResponse(url=original_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
