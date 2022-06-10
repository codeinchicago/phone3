from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Speak secrets'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from . import routes, models