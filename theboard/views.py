from flask import flash, redirect, url_for, render_template

from theboard import app, db
from theboard.models import Message
from theboard.forms import BoardForm

@app.route('/', methods = ['GET', 'POST'])
def index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = BoardForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('发送成功！👐🙌👌')
        return redirect(url_for('index'))
    return render_template('index.html', form = form, messages = messages) 