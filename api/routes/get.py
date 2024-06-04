from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from database.recommend import get_db
from crud.post import get_recommend_post
from crud.recommend import get_similar_posts

load_dotenv()

router = APIRouter()

@router.get('/')
async def get(user_id: int, db: Session = Depends(get_db)):
    post_ids = get_similar_posts(db, user_id)
    posts = get_recommend_post(post_ids)
    return posts






