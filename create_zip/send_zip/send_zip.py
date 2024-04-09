from flask import request, jsonify, send_file

from config import output_path_mods
from create_zip.generate_zip.generate_zip import generate_zip_arhive
from database.main import *


async def get_zip():
    try:
        generate_zip_arhive()
        return send_file(f"{output_path_mods}\mods.zip", as_attachment=True), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400