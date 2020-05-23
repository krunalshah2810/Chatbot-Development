from myproject import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__= 'user'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.Text)
    useremail =db.Column(db.Text)
    userpass=db.Column(db.Text)

    projects=db.relationship('Project',backref='user',lazy=False)

    def __init__(self,username,useremail,userpass):
        self.username = username
        self.useremail= useremail
        self.userpass = generate_password_hash(userpass)


    def check_password(self,userpass):
        return check_password_hash(self.userpass,userpass)


#############################################

class Project(db.Model):

        __tablename__= 'project'
        projectid=db.Column(db.Integer,primary_key=True)
        projectname = db.Column(db.Text)
        userid =db.Column(db.Integer,db.ForeignKey('user.id'))
        intents=db.relationship('Intent',backref='project')
        entities = db.relationship('Entity',backref='project')

        def __init__(self,projectname,userid,token
        ):
            self.projectname = projectname
            self.userid= userid
            self.token = token



###############################################3
class Intent(db.Model):

    __tablename__= 'intent'
    intentid=db.Column(db.Integer,primary_key=True)
    intentname = db.Column(db.Text)
    projectid =db.Column(db.Integer,db.ForeignKey('project.projectid'))
    responses=db.relationship('Response',backref='intent')
    userqueries = db.relationship('User_query',backref='intent')

    def __init__(self,intentname,projectid):
        self.intentname = intentname
        self.projectid= projectid


class Entity(db.Model):

    __tablename__= 'entity'
    entityid=db.Column(db.Integer,primary_key=True)
    entityname = db.Column(db.Text)
    projectid =db.Column(db.Integer,db.ForeignKey('project.projectid'))
    values=db.relationship('Value',backref='entity')

    def __init__(self,entityname,projectid):
        self.entityname = entityname
        self.projectid= projectid


class Value(db.Model):

    __tablename__ = 'value'
    valueid = db.Column(db.Integer,primary_key=True)
    valuename = db.Column(db.Text)
    synonym = db.Column(db.Text)
    entity_id =db.Column(db.Integer,db.ForeignKey('entity.entityid'))

    def __init__(self,valuename,synonym,entityid):
        self.valuename = valuename
        self.synonym = synonym
        self.entitytid= entityid




###############################################
class Response(db.Model):

    __tablename__= 'response'
    responseid=db.Column(db.Integer,primary_key=True)
    responsename = db.Column(db.Text)
    intenttid =db.Column(db.Integer,db.ForeignKey('intent.intentid'))

    def __init__(self,responsename,intentid):
        self.responsename = responsename
        self.intenttid= intentid

class User_query(db.Model):

    __tablename__= 'user_query'
    queryid=db.Column(db.Integer,primary_key=True)
    queryname = db.Column(db.Text)
    intenttid =db.Column(db.Integer,db.ForeignKey('intent.intentid'))

    def __init__(self,queryname,intentid):
        self.queryname = queryname
        self.intenttid= intentid


if __name__ == '__main__':
    app.run(debug=True)
