
import datetime

from markdown import markdown

from dip.extensions import db

class WikiPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)

    content = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    owner_id = db.Column(db.ForeignKey('users.id'))
    owner = db.relationship('User', back_populates='wiki_pages')

    def json(self):
        return {
            'name': self.name,
            'slug': self.slug,
            'content': self.content,
            'html': markdown(self.content),
            'created_at': self.created_at,
            'owner_id': self.owner_id,
            'owner': self.owner.json()
        }