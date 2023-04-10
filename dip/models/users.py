from dip.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    photo = db.Column(db.String(255))

    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    phone_number = db.Column(db.String(11))
    job_title_id = db.Column(db.ForeignKey('job_titles.id'))
    job_title = db.relationship('JobTitle', back_populates='users')

    role = db.Column(db.String(50), nullable=False, default='user')

    wiki_pages = db.relationship('WikiPage', back_populates='owner')
    # documents 
    # applications

    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'patronymic': self.patronymic,
            'full_name': f'{self.first_name} {self.second_name} {self.patronymic}',
            'username': self.username,
            'photo': self.photo,
            'email': self.email,
            'phone_number': self.phone_number,
            'job_title': self.job_title.json() if self.job_title else None,
            'role': self.role,
        }


class JobTitle(db.Model):
    __tablename__ = 'job_titles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)

    users = db.relationship('User', back_populates='job_title')

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
        }