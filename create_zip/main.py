import asyncio
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from create_zip.send_zip.send_zip import get_zip
from file.delete_file.delete_file import delete_mods
from file.get_mods.get_mods import get_all_mods
from file.post_file.post_file import post_file_mods

upload_zip = Blueprint('upload_zip', __name__)


@upload_zip.route("/file/upload", methods=["GET", "OPTIONS"])
@cross_origin()
def get_user():
    if request.method == "GET":
        return asyncio.run(get_zip())
