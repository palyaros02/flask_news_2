# Новостной портал

Новосной сайт, на котором можно просматривать новости, добавлять новости, редактировать и удалять новости.

## Описание

Новостной сайт, созданный с помощью Flask на Python в рамках курса Python Pro

## Технологии

* [Python 3.11](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [SQLAlchemy 1.4](https://docs.sqlalchemy.org/en/14/index.html)
* [SQLite](https://www.sqlite.org/index.html)
* [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)

## Как запустить

1. Склонировать репозиторий `git clone https://github.com/palyaros02/flask_news_2.git`
2. Создать и активировать виртуальное окружение
```bash
python -m venv ./.venv
source .venv/bin/activate # для Linux
.venv\Scripts\activate # для Windows
```
3. Установить зависимости 
```bash
pip install -r requirements.txt
```
4. Переименуйте файл `.env.example` в `.env` и заполните его своими значениями.
5. Запустить приложение
```bash
flask run
```
