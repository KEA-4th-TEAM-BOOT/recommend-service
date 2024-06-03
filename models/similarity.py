from sqlalchemy import Column, Integer, Float
from database.recommend import Base

class Similarity(Base):
    __tablename__ = 'similarities'

    similarity_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    similarity = Column(Float, nullable=False)
