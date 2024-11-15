import os
from datetime import timedelta
from dotenv import load_dotenv



basedir = os.path.abspath(os.path.dirname(__file__))

# Permet de charger le fichier d'environnement présent a la racine du projet
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "TODO App"
    API_VERSION = "v1"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class DevelopmentConfig(Config):
    # URL de connexion pour la BDD
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://azzed:mdpdeazzed@mysql/projet_docker_bdd")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)


# Health check pour vérifier qu'on se connecte a la BDD
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "mysql+pymysql://test_user:test_password@localhost/test_projet_docker_bdd")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
