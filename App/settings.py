# -*- coding: utf-8 -*-

def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    mysql = DATABASE.get('mysql') or 'pymysql'
    username = DATABASE.get('username') or 'root'
    password = DATABASE.get('password') or '123456'
    host = DATABASE.get('host') or 'localhost'
    port = DATABASE.get('port') or '3306'
    db = DATABASE.get('db') or 'Shopping'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)


class Config():
    TEST = False
    DEBUG = False
    SECRET_KEY = '110'
    # SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    UPLOAD_FOLDER = "/s/static"
    THUMBNAIL_FOLDER = "/s/thumb"
    UPLOADS_DEFAULT_URL = 'http://127.0.0.1:5000/'


class DevelopConfing(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':'3306',
        'db':'Shopping'
    }
    SQLALCHEMY_DATABASE_URI=get_database_uri(DATABASE)

env = {
    'develop':DevelopConfing
}