from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .basic import basic
    app.register_blueprint(basic, url_prefix='/basic')

    @app.route('/')
    def showz():
        return 'z'

    return app