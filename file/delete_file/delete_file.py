import datetime

from database.main import *
from flask import request, jsonify
import os

from file.get_mods.get_mods import get_all_mods


async def delete_mods():
    try:
        body = request.json
        result = session.query(mods).filter(mods.mod_name == body["name"])
        for i in result:
            os.remove(i.path_mod)
            create_date = datetime.datetime.today()
            session.query(mods).filter(mods.mod_name == body["name"]).delete()
            session.add(history(mod_name=i.path_mod, datetime=create_date, operation=2))
        session.commit()
        get_all_mods.cache_clear()
        return jsonify({"message": "Мод успешно удален"}), 200
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        print(e)
        return jsonify({"message": 'Некоректный формат фото!'}), 400
