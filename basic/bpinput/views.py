from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info
from .. import db
from .forms import EntryForm
from flask_login import login_required, current_user

bpinput = Blueprint('bpinput', __name__, template_folder='templates')

@bpinput.route('/', methods=['GET', 'POST'])
@bpinput.route('/input', methods=['GET', 'POST'])
@login_required
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        new_info = Info(data=form.info.data, user_id=current_user.id)
        db.session.add(new_info) 
        db.session.commit()
        return redirect(url_for('bpinput.entry'))
        #return render_template('i6.html', form=form)

    return render_template('i6.html', form=form)

  
