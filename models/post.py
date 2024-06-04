from pydantic import BaseModel
from typing import Optional, Any
from typing import List
from datetime import datetime

class Post(BaseModel):
    id: int
    userLink: str
    personalPostId: Optional[int]
    postVoiceFileUrl: Optional[str]
    categoryId: Optional[int]
    subCategoryId: Optional[int]
    subject: str
    title: str
    content: str
    thumbnail: Optional[str]
    thumbnailImageUrl: Optional[str]
    accessibility: str
    hitCnt: Optional[int]
    likeCnt: Optional[int]
    createdTime: Optional[datetime]
    comments: Any