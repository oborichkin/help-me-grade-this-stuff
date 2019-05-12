import pandas as pd

from help_me import app, db
from help_me.models import Answer, Question


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    que = pd.read_csv("data/que.csv", sep='|')
    ans = pd.read_csv("data/ans.csv", sep='|')

    for _, row in que.iterrows():
        q = Question(id=row['ID'],
                     text=row['QUESTIOIN'],
                     right_answer=row['TEACHER_ANSWER'])
        db.session.add(q)
    db.session.commit()

    for _, row in ans.iterrows():
        if row['ID'] == 9895:
            exit
        a = Answer(id=row['ID'],
                   q_id=row['Q_ID'],
                   text=row['ANSWER'])
        db.session.add(a)
    db.session.commit()
