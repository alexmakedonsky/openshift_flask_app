from .models import Post
from apps.core.database import write, read


def create_post(data):
    with write() as session:
        post = Post(**data)
        session.add(post)
    return post.to_dict()


def list_posts():
    with read() as session:
        posts = session.query(Post).all()
    return [post.to_dict() for post in posts]


def retrieve_post(post_pk):
    with read() as session:
        post = session.query(Post).filter(Post.id == post_pk).first()
    return post


def update_post(pk, data):
    with write() as sesseion:
        post = sesseion.query(Post).filter_by(id=pk).first()
        post.text = data["text"]
        post.title = data['title']
    return post.to_dict()


def delete_post(pk):
    with write() as session:
        post = session.query(Post).filter_by(id=pk).delete()
    return {"msg": "Post was deleted successfully"}
