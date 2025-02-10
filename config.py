import os
import redis
import json

class Config(object):
    # Определяет, включен ли режим отладки
    # В случае если включен, flask будет показывать
    # подробную отладочную информацию. Если выключен -
    # - 500 ошибку без какой либо дополнительной информации.
    DEBUG = False
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True
    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    URL = os.environ.get("URL")

    SESSION_COOKIE_SECURE = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_SERIALIZATION_FORMAT = "json"
    # Для подключения к Redis, используйте имя хоста контейнера
    REDIS_HOST = os.environ.get("REDIS_HOST", "flask_redis")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)



class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

def init_redis(app):
    """Инициализация подключения к Redis после создания Flask-приложения"""
    app.config["SESSION_REDIS"] = redis.StrictRedis(
        host=app.config["REDIS_HOST"],
        port=app.config["REDIS_PORT"],
        decode_responses=True
    )
