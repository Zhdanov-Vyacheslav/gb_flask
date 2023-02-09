from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

from gb_web.extensions import db


class Author(db.Model):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")

    def __str__(self):
        return self.user.email
