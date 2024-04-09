from functools import lru_cache

from flask import request, jsonify

from database.main import *


@lru_cache(maxsize=2)
def get_all_mods():
    try:
        mods_all = []
        check_mods = session.query(mods).all()
        for i in check_mods:
            mods_all.append({"id": i.id, "name": i.mod_name})
        return jsonify({"mods": mods_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400