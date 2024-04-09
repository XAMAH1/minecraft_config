import datetime

from database.main import *
from flask import request, jsonify
from config import picture_path
import os

from file.get_mods.get_mods import get_all_mods

image_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', "jar"]


async def post_file_mods():
    try:
        cur_file = request.form["name"].split("\\")[-1]
        file = request.files['file']
        result = session.query(mods).filter(mods.mod_name == f'{cur_file}')
        for i in result:
            return jsonify({"message": "Ошибка! Этот мод уже есть!"}), 400
        if not file:
            return jsonify({"message": "Выберите мод "}), 400
        if cur_file.split(".")[-1] not in image_formats:
            return jsonify({"message": "Не поддерживаемый формат мода"}), 400
        try:
            new_path = os.path.join(picture_path, f'{cur_file}')
            create_date = datetime.datetime.today()
            session.add(mods(mod_name=f'{cur_file}', path_mod=new_path, datetime=create_date, ))
            session.add(history(mod_name=new_path, datetime=create_date, operation=1))
            file.save(f"{new_path}")
            file.close()
            session.commit()
            get_all_mods.cache_clear()
            return jsonify({"message": "Мод успешно добавлен"}), 200
        except Exception as e:
            try:
                session.rollback()
            except:
                pass
            return jsonify({"message": 'Некоректный формат мода!'}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Выберите мод"}), 400