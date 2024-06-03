from sqlalchemy.orm import Session
from models.similarity import Similarity as SimilarityModel
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
