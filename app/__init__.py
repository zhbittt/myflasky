from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth.auth import Auth

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key="lmw"

    # 设置配置文件
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    Auth(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
