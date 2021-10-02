from app import db

class UserTable(db.Model):
    __tablename__ = 'User'

    username = db.Column(db.String(256),primary_key=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(128),unique=True)
    mobile = db.Column(db.String(14))

    def __init__(self,username,password,email,mobile):
        self.username = username
        self.password = password
        self.email = email
        self.mobile = mobile

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self,password):
        return self.password == password
    
    @classmethod
    def login_user(cls,username,password):
        user = cls.query.filter_by(username=username).first()
        if user == None:
            return None
        if user.check_password(password):
            return user
