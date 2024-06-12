from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.recommend import get_db
from crud.post import get_recommend_post
from crud.recommend import get_similar_posts, get_similar_posts_by_post

router = APIRouter()

@router.get('/{user_id}')
async def get(user_id: int, db: Session = Depends(get_db)):
    post_ids = get_similar_posts(db, user_id)
    posts = get_recommend_post(post_ids)
    return posts

@router.get('/post/{post_id}')
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post_ids = get_similar_posts_by_post(db, post_id)
    posts = get_recommend_post(post_ids)
    return posts




