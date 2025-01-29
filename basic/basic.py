from flask import Blueprint, render_template,  redirect, url_for, request


basic = Blueprint('basic', __name__, template_folder='templates')

@basic.route('/')
def home():
    return render_template('index.html')

@basic.route('/st')
def showzm():
	return 'zm'

@basic.route('/<name>')
def user(name):
	return render_template('i1.html', name=name)

@basic.route('/info', methods=['POST', 'GET'])
def getinfo():
    if request.method == 'POST':
        info = request.form['info']
        return redirect(url_for('basic.getinfo', info=info))
    else:
        return render_template('info.html')
    
@basic.route('/i4')
def i4():
    return render_template('i1.html', name='zm')

