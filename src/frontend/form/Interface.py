from flask_wtf import FlaskForm
from wtforms.fields import StringField, RadioField, SubmitField, FileField, SelectField
from wtforms.widgets import ListWidget, RadioInput
from wtforms.validators import DataRequired

class InterfaceForm(FlaskForm):
    folder = StringField('Type Directory of Folder', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    algorithm = RadioField('Choose Algorithm', coerce= int, choices=[(1, 'Booyer-Moore'), (2, 'Knuth-Morris-Pratt'), (3, 'Regex')], validators=[DataRequired()])
    submit = SubmitField('Extrac Info')