from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.config['SECRET_KEY'] = '****'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .basic import basic
    app.register_blueprint(basic, url_prefix='/basic')
    from .views import views
    app.register_blueprint(views, url_prefix='/views')

    from .models import Info
    
    @app.route('/')
    def showz():
        return 'z'
    
    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('basic/' + DB_NAME):
        db.create_all(app=app)
        print('db created')


