import os
import subprocess
import asyncio
from flask import Blueprint, request, jsonify, render_template
from flask_cors import cross_origin


user_console = Blueprint('user_console', __name__)


process = None
def start_process():
    global process
    if process is None or process.poll() is not None:
        process = subprocess.Popen(['C:\\Users\\XAMAH-SERVER\\Desktop\\Minecraft Server\\start.bat'], stdout=subprocess.PIPE, shell=True)


def stop_process():
    global process
    if process is not None and process.poll() is None:
        process.terminate()
        process = None
    os.system("Taskkill /IM java.exe /F")
    os.system("Taskkill /IM OpenConsole.exe /F")
    os.system("Taskkill /IM WindowsTerminal.exe /F")



@user_console.route('/server/start', methods=["GET"])
def index():
    start_process()
    return jsonify({"message": "Запустил"})


@user_console.route('/server/stop', methods=["GET"])
def stop_proc():
    stop_process()
    return jsonify({"message": "Остановил"})
