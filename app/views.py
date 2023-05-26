from flask import redirect, render_template, url_for

from . import app, db
from .models import Category, News
from .forms import NewsForm

@app.route('/')
def index():
    news = News.query.all()
    categories = Category.query.all()

    return render_template (
        'index.html',
        news=news[::-1],
        categories=categories
    )


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_item = News.query.get(id)
    categories = Category.query.all()

    return render_template (
        'news_detail.html',
        news=news_item,
        categories=categories
    )

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    categories = Category.query.all()
    form = NewsForm()

    if form.validate_on_submit():
        news_item = News(
            title=form.title.data,
            text=form.text.data,
            category_id=form.categories.data
        )
        db.session.add(news_item)
        db.session.commit()
        return redirect(url_for('add_news'))

    return render_template (
        'add_news.html',
        form=form,
        categories=categories
    )

@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template (
        'category.html',
        news=news,
        category_name=category_name,
        categories=categories
    )