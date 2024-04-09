import asyncio
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from file.delete_file.delete_file import delete_mods
from file.get_mods.get_mods import get_all_mods
from file.post_file.post_file import post_file_mods

user_profile = Blueprint('user_profile', __name__)


@user_profile.route("/file", methods=["POST", "DELETE", "GET", "OPTIONS"])
@cross_origin()
def get_user():
    if request.method == "POST":
        return asyncio.run(post_file_mods())
    if request.method == "GET":
        return get_all_mods()
    if request.method == "DELETE":
        return asyncio.run(delete_mods())
    if request.method == 'OPTIONS':
        # Возвращаем правильные заголовки CORS для предварительного запроса
        response = jsonify({'message': 'CORS request allowed'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response
