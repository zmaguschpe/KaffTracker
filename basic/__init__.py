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

    from .models import Info


    from .vi.vi import vi
    app.register_blueprint(vi, url_prefix='/vi')

    from .bp2.bp2views import bp2
    app.register_blueprint(bp2, url_prefix='/bp2')

    from .getdata.views import getdata
    app.register_blueprint(getdata, url_prefix='/')


    
    
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


