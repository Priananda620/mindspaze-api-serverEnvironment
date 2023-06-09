from flask import Flask
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate
from logging import getLogger
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

from .blueprints import mindspaze_bp
from .blueprints.prediction import prediction_blueprint
from .config import Config

app_logger = getLogger('app')
error_logger = getLogger('error')

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
scheduler = APScheduler()



def create_appp(test: bool = False) -> Flask:
    app = Flask("MindSpaze")
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        migrate.init_app(app, db)

        app.register_blueprint(mindspaze_bp)
        app.register_blueprint(prediction_blueprint)

        return app
