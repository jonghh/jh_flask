from jh_flask import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) # 기존 모델 연결, 삭제 연동 설정(답변도 함께 삭제)
    question = db.relationship('Question', backref=db.backref('answer_set'))  # 기존 모델 참조, 역참조(질문에 달린 답변들도 참조)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)