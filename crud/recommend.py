from typing import List
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.similarity import Similarity as SimilarityModel
from models.post_similarity import PostSimilarity as PostSimilarityModel
from schemas.similarity import Similarity as SimilaritySchema

def upsert_similarity(db: Session, similarity: SimilaritySchema):
    db_similarity = db.query(SimilarityModel).filter(
        SimilarityModel.user_id == similarity.user_id,
        SimilarityModel.post_id == similarity.post_id
    ).first()

    if db_similarity:
        db_similarity.similarity = similarity.similarity
    else:
        db_similarity = SimilarityModel(
            user_id=similarity.user_id,
            post_id=similarity.post_id,
            similarity=similarity.similarity
        )
        db.add(db_similarity)

    db.commit()
    db.refresh(db_similarity)

def upsert_similarity_by_post(db: Session, similarity: SimilaritySchema):
    db_similarity = db.query(SimilarityModel).filter(
        SimilarityModel.user_id == similarity.user_id,
        SimilarityModel.post_id == similarity.post_id
    ).first()

    if db_similarity:
        db_similarity.similarity = similarity.similarity
    else:
        db_similarity = SimilarityModel(
            user_id=similarity.user_id,
            post_id=similarity.post_id,
            similarity=similarity.similarity
        )
        db.add(db_similarity)

    db.commit()
    db.refresh(db_similarity)

def get_similar_posts(db: Session, user_id: int) -> List[int]:
    similar_posts = db.query(SimilarityModel.post_id).filter(
        SimilarityModel.user_id == user_id
    ).order_by(desc(SimilarityModel.similarity)).limit(4).all()

    post_ids = [post_id for (post_id,) in similar_posts]
    return post_ids

def get_similar_posts_by_post(db: Session, post_id: int) -> List[int]:
    similar_posts = db.query(PostSimilarityModel.post2_id).filter(
        PostSimilarityModel.post1_id == post_id
    ).order_by(desc(PostSimilarityModel.similarity)).limit(5).all()

    post_ids = [post_id for (post_id,) in similar_posts]
    return post_ids
