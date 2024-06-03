from pydantic import BaseModel

class Similarity(BaseModel):
    user_id: int
    post_id: int
    similarity: float