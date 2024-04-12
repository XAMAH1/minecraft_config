from functools import lru_cache
from os import walk
from flask import request, jsonify

from config import picture_path
from database.main import *


@lru_cache(maxsize=2)
def get_all_mods():
    try:
        mods_all = []
        md = []
        for (dirpath, dirnames, filenames) in walk(picture_path):
            md = filenames
        for i in md:
            mods_all.append({"id": 1, "name": i})
        return jsonify({"mods": mods_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
