# -*- coding: utf-8 -*-

APP_NAME = 'devops_server_test'

DEBUG = False

FAKE_SALT = False

SERVER_IP = '0.0.0.0'
SERVER_PORT = 8211

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hjx:123456@119.29.141.207:3306'
SQLALCHEMY_BINDS = {
    'devops': '%s/ywdb_li?charset=utf8mb4' % SQLALCHEMY_DATABASE_URI
}
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 3500

NAME_SERVER_URL = 'http://ans.huishoubao.com.cn'
NAME_SERVER_ID = '900001'
NAME_SERVER_KEY = 'wTQZ9U6LO8olNEykCGqvQB5UUPlY6MUj'