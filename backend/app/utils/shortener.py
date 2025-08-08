import hashlib
from datetime import datetime

def generate_short_code(original_url: str) -> str:
    """
    Generates a short code from the original URL and current timestamp.
    """
    # Combine URL with current time for uniqueness
    unique_string = f"{original_url}{datetime.now().isoformat()}"
    
    # Create a SHA256 hash
    hasher = hashlib.sha256(unique_string.encode())
    
    # Return the first 7 characters of the hex digest
    return hasher.hexdigest()[:7]
