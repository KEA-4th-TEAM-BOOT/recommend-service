from pydantic import BaseModel

class PostSimilarity(BaseModel):
    post1_id: int
    post2_id: int
    similarity: float