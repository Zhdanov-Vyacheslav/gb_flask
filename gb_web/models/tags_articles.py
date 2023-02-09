from sqlalchemy import Table, ForeignKey, Column, Integer

from ..extensions import db

tags_articles = Table(
    "tags_articles",
    db.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tags.id"), nullable=False)
)