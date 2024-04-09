
from flask import *

from config import API_HOST, API_PORT
from console.main import user_console
from create_zip.generate_zip.generate_zip import generate_zip_arhive
from create_zip.main import upload_zip
from file.main import user_profile
from flask_cors import CORS, cross_origin

from open_html.main import page_user

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.register_blueprint(user_profile, url_prefix="/api")
app.register_blueprint(user_console, url_prefix="/api")
app.register_blueprint(upload_zip, url_prefix="/api")
app.register_blueprint(page_user, url_prefix="/view")


@app.errorhandler(404)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error path request"}, 404


@app.errorhandler(405)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error method request"}, 404


@app.errorhandler(500)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": f"Возникла критическая ошибка сервера. Debug: {error}"}, 500


if __name__ == "__main__":
    app.run(debug=False, host=API_HOST[0], port=API_PORT)
