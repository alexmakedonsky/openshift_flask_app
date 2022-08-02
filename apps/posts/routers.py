import json
from flask import request, jsonify
from . import posts
from .views import create_post, list_posts, retrieve_post, update_post, delete_post


@posts.route("/create", methods=["POST"])
def post_create():
    data = json.loads(request.data)
    return jsonify(create_post(data))


@posts.route("/list", methods=["GET"])
def post_list():
    return jsonify(list_posts())


@posts.route("/retrieve/<int:post_pk>", methods=["GET"])
def post_retrieve(post_pk):
    post = retrieve_post(post_pk)
    if not post:
        return {"error": "Post not found"}, 404
    return jsonify(post.to_dict())


@posts.route("/update/<int:post_pk>", methods=["PUT"])
def post_update(post_pk):
    data = json.loads(request.data)
    return jsonify(update_post(post_pk, data))


@posts.route("/delete/<int:post_pk>", methods=["DELETE"])
def post_delete(post_pk):
    return jsonify(delete_post(post_pk))
