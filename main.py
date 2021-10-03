from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp
from translator import Translate
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("MY_SECRET_KEY")


class MyForm(FlaskForm):
    string_text = StringField(
        label="Add some text including letters, numbers, spaces, commas, or question marks. Other special characters are prohibited:", validators=[DataRequired(), Regexp(regex="^[a-zA-Z0-9 ?.,]*$", message="Provide a text including letters, numbers, spaces, commas, or question marks. Other special characters are prohibited!")])
    morse_text = StringField(label="Morse code:")
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
    elif form.reset.data:
            form["string_text"].data = ""
            form["morse_text"].data = ""
    else:
        flash(form.string_text.errors)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
