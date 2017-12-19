from re import findall

from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from nltk.corpus import stopwords
from nltk.stem.porter import *
from scipy.sparse import load_npz
from werkzeug.utils import redirect
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')
STOPWORDS = stopwords.words('english')


class SearchForm(FlaskForm):
    words = StringField('words', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def login():
    form = SearchForm()
    if form.validate_on_submit():
        words = stem_words(form.words.data)
        indexes = []
        for word in words:
            if vocabulary.get(word, None) is not None:
                indexes.append(vocabulary.get(word))
        for message in indexes:
            flash(message)
        return redirect('/results')
    return render_template('search.html', title='Search', form=form)


@app.route('/results')
def index():
    return render_template("results.html", title='Home')


def stem_words(line):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in map(lambda w: w.lower(), findall(r'\w+', line)) if word not in STOPWORDS]


# def find_most_similar(words, k=10):
# for column in matrix.T:


if __name__ == '__main__':
    with open('resources/vocabulary.txt', 'r', encoding='utf8') as vocabulary:
        vocab = vocabulary.readline().split(' ')
    vocabulary = {v: i for i, v in enumerate(vocab)}
    # matrix = load_npz('resources/org_matrix.npz')
    app.run()
