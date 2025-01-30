from flask import Blueprint, render_template, request, redirect, url_for
from .models import Info
from . import db

views = Blueprint('views', __name__)


@views.route('/infos', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
def infos():
    if request.method == 'POST': 
        info = request.form.get('info') 
        new_info = Info(data=info) 
        db.session.add(new_info) 
        db.session.commit()
        return render_template('i5.html', info=info)


    return render_template('i5.html', info='z')


  
