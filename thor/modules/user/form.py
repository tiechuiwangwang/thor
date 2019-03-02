from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class SigninForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(6, 32),
        ]
    )
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(6, 32),
        ]
    )


class SignupForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(6, 32),
        ]
    )
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(6, 32),
        ]
    )
    nickname = StringField(
        validators=[
            InputRequired(),
            Length(min=6),
        ]
    )
