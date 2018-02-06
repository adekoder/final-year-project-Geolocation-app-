from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_option):
    app = Flask(__name__)
    app.config.from_object(config[config_option])

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .models import Location, Category

    return app
    
