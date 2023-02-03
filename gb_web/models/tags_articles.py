from sqlalchemy import Table, ForeignKey

from ..extensions import db

tags_articles = Table(
    "tags_articles",
    db.metadata,
    db.Column("article_id", db.Integer, ForeignKey("articles.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tags.id"), nullable=False)
)