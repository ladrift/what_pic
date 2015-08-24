from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class ImageUrlForm(Form):
    url = StringField('Please input URL for pictures', validators=[Required()])
    submit = SubmitField('Submit')
