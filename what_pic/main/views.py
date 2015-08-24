from flask import render_template, session, url_for, current_app, redirect
from . import main
from .forms import ImageUrlForm
from ..cloud_sight import cloud_sight

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ImageUrlForm()
    if form.validate_on_submit():
        result = cloud_sight(form.url.data)
        if result:
            session['url'] = form.url.data
            session['result'] = result
        return redirect(url_for('.index'))

    return render_template('index.html',
                          form=form, result=session.get('result'),
                          url=session.get('url'))
