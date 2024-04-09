import subprocess
import asyncio
from flask import Blueprint, request, jsonify, render_template
from flask_cors import cross_origin


user_console = Blueprint('user_console', __name__)


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout


@user_console.route('/console', methods=["GET"])
def index():
    command_output = run_command("C:\\Users\\Ilya_\\PycharmProjects\\minecraft_config\\start.bat")
    return render_template('C:\\Users\\Ilya_\\PycharmProjects\\minecraft_config\\two.html', output=command_output)
