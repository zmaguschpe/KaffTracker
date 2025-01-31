from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db

bp2 = Blueprint('bp2', __name__, template_folder='templates')


@bp2.route('/', methods=['GET', 'POST'])
def fb2():
    if request.method == 'POST': 
        info = request.form.get('info') 
        new_info = Info(data=info) 
        db.session.add(new_info) 
        db.session.commit()
        return render_template('i7.html', info=info)


    return render_template('i7.html', info='bp2')


  
