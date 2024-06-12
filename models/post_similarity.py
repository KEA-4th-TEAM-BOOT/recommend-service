from sqlalchemy import Column, Integer, Float
from database.recommend import Base

class PostSimilarity(Base):
    __tablename__ = 'post_similarities'

    post_similarity_id = Column(Integer, primary_key=True, autoincrement=True)
    post1_id = Column(Integer, nullable=False)
    post2_id = Column(Integer, nullable=False)
    similarity = Column(Float, nullable=False)
