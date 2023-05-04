from flask import Blueprint
from flask_restful import Api

from mindspaze_api.resources.prediction import (
    PredictionResource,
)

prediction_blueprint = Blueprint("prediction", __name__, url_prefix="/predict")
prediction_api = Api(prediction_blueprint)

prediction_api.add_resource(PredictionResource, "")
