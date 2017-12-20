from re import findall

from sortedcontainers import SortedList
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
        columns = find_most_similar(words)
        for column in columns:
            print(column[1])
            flash(texts[column[0]])
        return redirect('/results')
    return render_template('search.html', title='Search', form=form)


@app.route('/results')
def index():
    return render_template("results.html", title='Home')


def stem_words(line):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in map(lambda w: w.lower(), findall(r'\w+', line)) if word not in STOPWORDS]


def find_most_similar(words, k=10):
    indexes = []
    for word in words:
        if vocabulary.get(word, None) is not None:
            indexes.append(vocabulary.get(word))
    l = []
    for num, column in enumerate(matrix.toarray().T):
        if num % 100 == 0: print(num)
        sum = 0
        for index in indexes:
            sum += column[index]
        l.append((num, sum))
        if len(l) > k:
            l.sort(key=lambda x: x[1], reverse=True)
            l.pop()
    return l


if __name__ == '__main__':
    with open('resources/training_set_tweets_clean_3-copy.txt', 'r', encoding='utf8') as read_file:
        texts = read_file.read().splitlines()[:30_000]
    with open('resources/vocabulary-copy.txt', 'r', encoding='utf8') as vocabulary:
        vocab = vocabulary.readline().split(' ')
    vocabulary = {v: i for i, v in enumerate(vocab)}
    # matrix = load_npz('resources/org_matrix-copy.npz')
    matrix = load_npz('resources/cln_sparse_matrix.npz')
    # matrix = load_npz('resources/org_nonscale_but_normalise_matrix.npz').toarray().T
    app.run()
