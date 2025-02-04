from flask import Blueprint, render_template #,  request, redirect, url_for
from ..models import Info
from .. import db
from flask_login import login_required, current_user

bpshow = Blueprint('bpshow', __name__, template_folder='templates')


@bpshow.route('/show')
@login_required
def show():
    return render_template('show.html', user=current_user)


  
