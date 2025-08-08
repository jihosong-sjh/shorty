from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    pass

class URLInfo(URLBase):
    short_code: str
