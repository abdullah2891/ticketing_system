from flask import Flask,request 
from flask_restful import Api, Resource 
from  user import db,Issue

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:toor@localhost/jira'

db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

class IssueRequest(Resource):
    def get(self):
        issues = Issue.query.all()
        Issues = []
        for issue in issues:
            Issues.append({"title" : issue.__dict__['title'],
                           "description" : issue.__dict__['description']
                          })


        return {'status':'ok','Issues': Issues}

    def post(self):
        issue = request.get_json()
        newIssue = Issue(issue["title"],issue["description"])
        db.session.add(newIssue)
        db.session.commit()
        return {"status":"ok", "status":"Issue created"}


api.add_resource(IssueRequest, '/issue')

if __name__ == '__main__':
    app.run(debug=True)

