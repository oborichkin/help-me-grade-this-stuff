from help_me import db


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    q_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text)
    correct = db.Column(db.Boolean)

    def __repr__(self):
        return f"Answer ({self.id})"


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    right_answer = db.Column(db.Text)

    answers = db.relationship('Answer', backref='question')

    def __repr__(self):
        return f"Question ({self.id})"
