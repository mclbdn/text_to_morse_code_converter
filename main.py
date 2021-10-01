import re
from flask import Flask, render_template
from flask.helpers import url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from translator import Translate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'


class MyForm(FlaskForm):
    string_text = StringField(
        label="Add a string text including spaces, commas, or question marks. Other special characters are prohibited:", validators=[DataRequired()])
    morse_text = StringField(label="Morse text:")
    submit = SubmitField(label="Submit")
    reset = SubmitField(label="Reset")


@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        if form.submit.data:
            string_text = form["string_text"].data
            translate = Translate(string_text)
            morse_code = translate.print_morse()
            form["morse_text"].data = morse_code
        elif form.reset.data:
            form["string_text"].data = ""
            form["morse_text"].data = ""

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
