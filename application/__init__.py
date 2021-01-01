from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes  
        db.create_all()

        return app