from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db

bpshow = Blueprint('bpshow', __name__, template_folder='templates')


@bpshow.route('/show')
def show():
    found_info = Info.query.all()
    return render_template('show.html', info=found_info)


  
