from datetime import datetime

from . import db

class Category(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    news = db.relationship('News', back_populates='category')

    def __repr__(self):
        return f'<Category({self.id=}, {self.title=})>'

class News(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    category = db.relationship('Category', back_populates='news')

    def __repr__(self):
        return f'<News({self.id=}, {self.title=}, {self.text=}, {self.created_date=}, {self.category=})>'