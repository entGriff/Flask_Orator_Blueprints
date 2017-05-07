from flask import Blueprint, request
from user.models import User
from flask_orator import Orator, jsonify


user_app = Blueprint('user_app', __name__)
 

@user_app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())

    return jsonify(user)


@user_app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user)


@user_app.route('/users', methods=['GET'])
def get_all_users():
    users = User.all()

    return jsonify(users)


@user_app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())

    return jsonify(user)


@user_app.route('/users/<int:user_id>/messages', methods=['GET'])
def get_user_messages(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user.messages)


@user_app.route('/users/<int:user_id>/messages', methods=['POST'])
def create_message(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user.messages().create(**request.get_json()))


@user_app.route('/users/<int:user_id>/following', methods=['GET'])
def get_user_following(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user.followed)


@user_app.route('/users/<int:user_id>/followers', methods=['GET'])
def get_user_followers(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user.followers)


@user_app.route('/users/<int:user_id>/following/<int:followed_id>', methods=['PUT'])
def follow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)

    user.follow(followed)

    return jsonify(followed.followers)

@user_app.route('/users/<int:user_id>/following/<int:followed_id>', methods=['DELETE'])
def unfollow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)

    user.unfollow(followed)

    return jsonify(followed.followers)