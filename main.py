from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route('/st')
def showzm():
	return 'zm'

@app.route("/<name>")
def user(name):
	return render_template('i1.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)