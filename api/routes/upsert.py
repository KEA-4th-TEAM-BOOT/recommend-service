from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.recommend import get_db
from crud.elastic import get_posts
from crud.like import make_user
from crud.recommend import upsert_similarity
from core.clean import clean_data
from core.inference import request_endpoint

router = APIRouter()

@router.post('/')
async def upsert(user_id: int, db: Session = Depends(get_db)):
    posts = get_posts()

    posts = clean_data(posts, user_id)

    user = make_user(user_id)

    similarities = request_endpoint(user, posts)

    for similarity in similarities:
        upsert_similarity(db, similarity)

    return {"message": "Recommendation data successfully updated."}







