from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings.Config')

db = SQLAlchemy(app)

# Импортируем свои модули ТОЛЬКО ПОСЛЕ создания app и db
from . import views, error_handlers, cli_commands  # noqa: E402

with app.app_context():
    db.create_all()