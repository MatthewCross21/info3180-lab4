from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    file = FileField("Upload File", validators=[
        InputRequired(),
        FileAllowed(['jpg', 'png'], "Only JPG and PNG images")  
    ])
    submit = SubmitField("Upload")