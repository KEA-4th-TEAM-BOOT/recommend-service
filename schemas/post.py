from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    user_id: int
    content: str