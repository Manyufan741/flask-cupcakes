from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddCupcakeForm(FlaskForm):

    flavor = StringField("Flavor",  validators=[
                         InputRequired(message="Flavor can't be blank")])
    size = StringField("Size", validators=[
                       InputRequired(message="Size can't be blank")])
    rating = FloatField("Rating", validators=[
                        InputRequired(message="Rating can't be blank"), NumberRange(min=0, max=10)])
    image = StringField("Image", validators=[Optional()])


class UpdateCupcakeForm(FlaskForm):

    update_flavor = StringField("Flavor",  validators=[
        InputRequired(message="Flavor can't be blank")])
    update_size = StringField("Size", validators=[
        InputRequired(message="Size can't be blank")])
    update_rating = FloatField("Rating", validators=[
        InputRequired(message="Rating can't be blank"), NumberRange(min=0, max=10)])
    update_image = StringField("Image", validators=[Optional()])
