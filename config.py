#class Config:
#    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'joahan123'
    MYSQL_DB = 'loginUser'


config={
    'developmet':DevelopmentConfig
}