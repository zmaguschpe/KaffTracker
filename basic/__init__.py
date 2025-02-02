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

    


    from .bpinput.views import bpinput
    app.register_blueprint(bpinput, url_prefix='/')

    from .bp2.bp2views import bp2
    app.register_blueprint(bp2, url_prefix='/bp2')

    from .bpshow.views import bpshow
    app.register_blueprint(bpshow, url_prefix='/')

    from .errors import bp as errors_bp
    app.register_blueprint(errors_bp)


    
    
    @app.route('/z')
    def showz():
        return 'z'
    
    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('basic/' + DB_NAME):
        db.create_all(app=app)
        print('db created')


