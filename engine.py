from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')


class SearchForm(FlaskForm):
    words = StringField('words', validators=[DataRequired()])


@app.route('/search', methods=['GET', 'POST'])
def login():
    form = SearchForm()
    if form.validate_on_submit():
        flash('{}'.format(form.words.data))
        return redirect('/results')
    return render_template('search.html', title='Search', form=form)


@app.route('/')
@app.route('/results')
def index():
    return render_template("results.html", title='Home')


if __name__ == '__main__':
    app.run()
