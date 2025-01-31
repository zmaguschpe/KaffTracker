from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db

bpinput = Blueprint('bpinput', __name__, template_folder='templates')


@bpinput.route('/', methods=['GET', 'POST'])
def getinput():
    if request.method == 'POST': 
        info = request.form.get('info') 
        new_info = Info(data=info) 
        db.session.add(new_info) 
        db.session.commit()
        return render_template('i6.html', info=info)
    # -> redirect
    


    return render_template('i6.html', info='z')


  
