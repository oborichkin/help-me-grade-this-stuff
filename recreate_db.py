import pandas as pd

from help_me import app, db
from help_me.models import Answer, Question


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    que = pd.read_csv("data/que.csv", sep='|')
    ans = pd.read_csv("data/ans.csv", sep='|')

    row_limit = 10000

    for _, row in que.iterrows():
        if row_limit <= 0:
            break
        q = Question(id=row['ID'],
                     text=row['QUESTIOIN'],
                     right_answer=row['TEACHER_ANSWER'])
        db.session.add(q)
        row_limit -= 1
    db.session.commit()

    for _, row in ans.iterrows():
        if row_limit <= 0:
            break
        a = Answer(id=row['ID'],
                   q_id=row['Q_ID'],
                   text=row['ANSWER'])
        db.session.add(a)
        row_limit -= 1
    db.session.commit()
