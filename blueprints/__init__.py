from flask import Blueprint
from flask_restful import Api

from mindspaze_api.resources.banana import Banana
from mindspaze_api.resources.prediction import PredictionResource

mindspaze_bp = Blueprint("mindspaze_bp", __name__, url_prefix="/mindspaze_api")
mindspaze_api = Api(mindspaze_bp)

mindspaze_api.add_resource(Banana, "/banana")
# mindspaze_api.add_resource(PredictionResource, "/predict")
