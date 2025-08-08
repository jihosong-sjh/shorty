import redis

def get_url_by_code(db: redis.Redis, code: str) -> str | None:
    """Retrieves the original URL for a given short code."""
    url = db.get(code)
    return url if url else None

def save_url_mapping(db: redis.Redis, code: str, original_url: str) -> None:
    """Saves a new short code and original URL pair in the database."""
    db.set(code, original_url)
