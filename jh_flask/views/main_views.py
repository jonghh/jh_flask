from flask import Blueprint, render_template

from jh_flask.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Pybo index'

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/q')
def question():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)