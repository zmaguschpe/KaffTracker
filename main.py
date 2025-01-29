from flask import Flask, render_template, redirect, url_for, request
from basic import basic 

app = Flask(__name__)
app.register_blueprint(basic, url_prefix='/basic')

@app.route('/')
def showz():
    return 'z'

if __name__ == '__main__':
    app.run(debug=True)