from apps.core.database import db
from sqlalchemy import Column, Integer, String


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(64), unique=True)
    text = Column(String(128), )
    # author =

    def to_dict(self):
        return dict(id=self.id, title=self.title, text=self.text)


class User(db.Model):
    __tablename__ = 'user'
    # post_id =
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    email = Column(String(48), unique=True)

    def to_dict(self):
        return dict(id=self.id, namae=self.name, email=self.email)