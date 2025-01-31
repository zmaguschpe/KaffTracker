from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db

getdata = Blueprint('getdata', __name__)


@getdata.route('/zz')
def zz():
    return render_template('i1.html')


  
