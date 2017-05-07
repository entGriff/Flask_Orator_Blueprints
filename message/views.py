from flask import Blueprint, request
from flask_orator import jsonify
from message.models import Message

message_app = Blueprint('message_app', __name__)

@message_app.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.find_or_fail(message_id)

    return jsonify(message)


@message_app.route('/messages/<int:message_id>', methods=['PATCH'])
def update_message(message_id):
    message = Message.find_or_fail(message_id)
    message.update(**request.get_json())

    return jsonify(message)

@message_app.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.find_or_fail(message_id)
    message.delete()

    return jsonify({"result":"message deleted"})