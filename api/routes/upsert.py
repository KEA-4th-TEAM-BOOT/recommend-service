from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from database.recommend import get_db
from crud.post import get_post
from crud.recommend import upsert_similarity
from schemas.user import User
from core.clean import clean_data
from core.inference import request_endpoint

load_dotenv()

router = APIRouter()

@router.post('/')
async def upsert(user: User, db: Session = Depends(get_db)):
    posts = get_post()

    posts = clean_data(posts, user.user_id)

    similarities = request_endpoint(user, posts)

    for similarity in similarities:
        upsert_similarity(db, similarity)




