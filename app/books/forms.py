from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5 # type: ignore

from flask_wtf import FlaskForm, CSRFProtect # type: ignore
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField # type: ignore
from wtforms.validators import DataRequired, Length # type: ignore
from app.models import db


class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(2, 40)])
    image= FileField("Image", validators=[DataRequired()])
    num_of_pages = IntegerField("num_of_pages", validators=[DataRequired()])
    description = StringField("description")

    submit = SubmitField("Save new Post")

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)