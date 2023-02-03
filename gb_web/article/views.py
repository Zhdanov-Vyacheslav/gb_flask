from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from ..extensions import db
from ..forms.article import CreateArticleForm
from ..models import Author, Tag
from ..models.article import Article

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")


@article.route("/", methods=["GET"])
@login_required
def article_list():
    articles = Article.query.all()
    return render_template(
        "articles/list.html",
        articles=articles
    )


@article.route("/<int:pk>", methods=["GET"])
@login_required
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
    if _article is None:
        raise NotFound("Article id:{}, not found".format(pk))
    return render_template(
        "articles/details.html",
        article=_article
    )


@article.route("/tag/<int:pk>", methods=["GET"])
@login_required
def get_articles_by_tag(pk: int):
    _tag = Tag.query.filter_by(id=pk).options(joinedload(Tag.articles)).one_or_none()
    if _tag is None:
        raise NotFound("Article id:{}, not found".format(pk))
    _articles = _tag.articles
    return render_template(
        "articles/list.html",
        articles=_articles,
        tag=_tag.name
    )


@article.route("/create", methods=["GET"])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]

    return render_template("articles/create.html", form=form)


@article.route("/create", methods=["POST"])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        _article.author_id = current_user.author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for("article.get_article", pk=_article.id))
    return render_template("articles/create.html", form=form)
