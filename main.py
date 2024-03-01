from flask import Flask, render_template, request, redirect, url_for, flash
# pip install Flask
from flask_wtf import FlaskForm
# pip install Flask-WTF
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SHHHHH'


# Form for inputting a name, email and message with submit button
class NewForm(FlaskForm):
    name = StringField("Location Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=["POST", "GET"])
def home():
    form = NewForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash("Thank you for your message")
    return render_template('formPage.html', form=form)



#this allows us to run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)