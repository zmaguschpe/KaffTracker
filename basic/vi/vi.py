from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db

vi = Blueprint('vi', __name__, template_folder='templates')


@vi.route('/vi', methods=['GET', 'POST'])
@vi.route('/', methods=['GET', 'POST'])
def infos2():
    if request.method == 'POST': 
        info = request.form.get('info') 
        new_info = Info(data=info) 
        db.session.add(new_info) 
        db.session.commit()
        return render_template('i6.html', info=info)


    return render_template('i6.html', info='z')


  
