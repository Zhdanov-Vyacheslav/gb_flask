from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship

from gb_web.extensions import db
from gb_web.models.tags_articles import tags_articles


class Tag(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    articles = relationship("Article", secondary=tags_articles, back_populates="tags")



