from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(c.id, c.title) for c in categories]


class NewsForm(FlaskForm):
    title = StringField(
        'Заголовок новости',
        validators=[
            DataRequired(message='Поле не должно быть пустым'),
            Length(min=5, max=255, message='Длина строки должна быть от 5 до 255 символов')
        ]
    )
    text = TextAreaField(
        'Текст новости',
        validators=[
            DataRequired(message='Поле не должно быть пустым')
        ]
    )
    categories = SelectField('Категория',choices=get_categories())
    submit = SubmitField('Добавить новость')