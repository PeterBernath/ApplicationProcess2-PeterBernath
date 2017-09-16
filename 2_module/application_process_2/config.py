# This file is version controlled.
# After pulling it, you have to copy and create your 'config.py' out of it.


class Config:
    DB_NAME = "peter"
    DB_USER = "peter"
    DB_HOST = "localhost"
    DB_PWD = "honolulu"
    DB_CONNECTION_STR = "dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PWD + "'"
