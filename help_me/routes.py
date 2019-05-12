from flask import render_template, request, abort, redirect, url_for
from sqlalchemy import text
from sqlalchemy.sql import func, select
from help_me import app, db
from help_me.models import Answer, Question


total_query = select([func.count()]).select_from(text('answer'))
left_query = select([func.count()]).where(Answer.correct == None)

@app.route('/')
def home():
    answer = Answer.query.filter_by(correct = None).order_by(func.random()).first_or_404()
    total = db.session.execute(total_query).scalar()
    left = db.session.execute(left_query).scalar()
    done = total - left
    return render_template('index.html',
                            answer=answer,
                            left=left,
                            total=total,
                            done=done)


@app.route('/check/<int:answer_id>', methods=['POST'])
def check(answer_id):
    try:
        result = request.form['result']
        result = True if result == 'correct' else False
    except:
        abort(500)
    answer = Answer.query.get_or_404(answer_id)
    answer.correct = result
    db.session.commit()
    return redirect(url_for('home'))

