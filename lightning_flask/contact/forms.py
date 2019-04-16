from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email])
    subject = TextAreaField('Subject')
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')