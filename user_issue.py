from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100))
    description = db.Column(db.String(255))
    def __init__(self, title, description):
        self.title = title
        self.description = description

class IssueTags(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    primary_id = db.Column(db.Integer)
    tags = db.Column(db.String(50))
    def __init__(self,primary_id,  tags):
        self.tags = tags
        self.primary_id = primary_id
