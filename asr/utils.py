from flask import jsonify
from werkzeug.utils import secure_filename
import logging
import os


class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[37m',
        'INFO': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m',
        'CRITICAL': '\033[41m',
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = ColorFormatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def make_response(code=200, message="success", data=None):
    response = {"code": code, "message": message, "data": data}
    return jsonify(response)


def save_mp3_file(file, upload_folder="uploaded_files"):
    os.makedirs(upload_folder, exist_ok=True)

    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)

    file.stream.seek(0)
    file.save(file_path)

    return file_path
