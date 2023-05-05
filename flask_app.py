
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'


from flask import Flask
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate
from logging import getLogger
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

from mysite.blueprints import mindspaze_bp
from mysite.blueprints.prediction import prediction_blueprint
from config import Config

app_logger = getLogger('app')
error_logger = getLogger('error')

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
scheduler = APScheduler()


app = Flask("MindSpaze")
app.config.from_object(Config)

with app.app_context():
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(mindspaze_bp)
    # app.register_blueprint(prediction_blueprint)

    # return app
