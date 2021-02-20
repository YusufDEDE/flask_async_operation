from os import environ, path
from dotenv import load_dotenv
from datetime import datetime

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


def log_file_handle(log):
    with open(environ.get('LOG_FILE_NAME'), "a") as log_file:
        log_file.write(str(datetime.now()) + ' - ' + log + '\n')
