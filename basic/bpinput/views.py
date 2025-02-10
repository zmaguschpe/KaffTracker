from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Info, KtInfo, Tracker, User
from .. import db
from .forms import EntryForm, KtEntryForm
from flask_login import login_required, current_user

bpinput = Blueprint('bpinput', __name__, template_folder='templates')

@bpinput.route('/kth', methods=['GET', 'POST'])
@login_required
def kth():
    if request.method == 'POST':
        new_kt = KtInfo(user_id=current_user.id)
        db.session.add(new_kt) 
        db.session.commit()
        return redirect(url_for('.kth'))

    kts = current_user.kt
    if kts != []:
        lastdate=kts[-1].date
        cnt2 = 0
        for t in kts:
                if t.date==lastdate:
                    cnt2 += 1
        lastdate=str(lastdate)[6:]
    else:
        cnt2 = ""
        lastdate =""
    return render_template('ktinput_htm.html', cnt=cnt2, lastdate = lastdate)

@bpinput.route('/cshow')
def cshow():
    values = current_user.kt
    values.reverse()
    dates =[]
    datecounts = []
    for i in values:
            if i.date not in dates:
                dates.append(i.date)
    for date in dates:
        cnt4=0
        for i in values:
            if i.date == date:
                cnt4 += 1
        datecounts.append([date, cnt4])
    return render_template('cview.html', values=datecounts)


@bpinput.route('/ktt', methods=['GET', 'POST'])
@login_required
def ktt():
    if request.method == 'POST':
        item = request.form.get('item')
        cnt = request.form.get('cnt')
        new_ktrack = Tracker(item=item, cnt=cnt, user_id=current_user.id)
        db.session.add(new_ktrack) 
        db.session.commit()
        return redirect(url_for('.ktt'))

    return render_template('kt_t_input_htm.html')


@bpinput.route('/input', methods=['GET', 'POST'])
@login_required
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        new_info = Info(data=form.info.data, user_id=current_user.id)
        db.session.add(new_info) 
        db.session.commit()
        return redirect(url_for('bpinput.entry'))

    return render_template('i6.html', form=form)

@bpinput.route('/show')
@login_required
def show():
    return render_template('show.html', user=current_user)

@bpinput.route('/kshow')
@login_required
def kshow():
    return render_template('kshow.html', user=current_user)



@bpinput.route('/ktshow')
@login_required
def ktshow():
    return render_template('ktshow.html', user=current_user)


'''
@bpinput.route('/ktinput', methods=['GET', 'POST'])
@login_required
def ktentry():
    form = KtEntryForm()
    if form.validate_on_submit():
        new_kt = KtInfo(user_id=current_user.id)
        db.session.add(new_kt) 
        db.session.commit()
        return redirect(url_for('.ktentry'))

    return render_template('ktinput_wtf.html', form=form)
'''



  
