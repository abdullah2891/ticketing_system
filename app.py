from flask import Flask,request
from flask_restful import Api, Resource
from  user_issue  import db,Issue,IssueTags

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
            print issue.__dict__
            Issues.append({
                            "id" : issue.__dict__['id'],
                            "title" : issue.__dict__['title'],
                           "description" : issue.__dict__['description'],
                            "Tags" : list(map(lambda tag: tag.__dict__["tags"],
                                              db.session.query(IssueTags)
                                              .filter_by(primary_id = issue.__dict__['id'])))
                          })


        return {'status':'ok','Issues': Issues}

    def post(self):
        issue = request.get_json() 
        newIssue = Issue(issue["title"],issue["description"])
        db.session.add(newIssue)
        db.session.commit()
        return {"status":"ok", "status":"Issue created"}


class TagRequest(Resource):
    def get(self,id):
        tags = db.session.query(IssueTags).filter_by(primary_id=id).all()
        Tags = list(map(lambda tag: tag.__dict__['tags'],tags))
        return {"status":'ok',"Tags":Tags}


    def post(self,id):
        print id
        tag = request.get_json()
        newTag = IssueTags(id,tag["Tag"])
        db.session.add(newTag)
        db.session.commit()
        return {"status":"Tag Added"}

    def delete(self, id):
        deleteTag =  IssueTags.query.filter_by(id = id)
        db.session.delete(deleteTag)
        db.session.commit()
        return {"status":"ok"}

api.add_resource(IssueRequest, '/issue')
api.add_resource(TagRequest, '/issue/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)

