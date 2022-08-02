from flask import Blueprint
from .models import Post

posts = Blueprint("posts", __name__)

from apps.posts.routers import post_create
