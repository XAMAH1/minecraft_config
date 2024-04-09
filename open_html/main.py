import asyncio
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from file.delete_file.delete_file import delete_mods
from file.get_mods.get_mods import get_all_mods
from file.post_file.post_file import post_file_mods
from open_html.view_main_frame.main import main_frame

page_user = Blueprint('page_user', __name__)


@page_user.route("/page", methods=["GET"])
def get_user():
    if request.method == "GET":
        return asyncio.run(main_frame())
