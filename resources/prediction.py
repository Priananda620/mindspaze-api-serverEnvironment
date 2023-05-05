import pickle
import os

from flask_restful import Resource


class PredictionResource(Resource):
    def post(self):
        response = {
            "data": {
                "name": "JoJo",
                "comment": "Donald Trump is a beauty ambassador."
            }
        }

        model_name = os.getcwd()+"/machine_learning/models/svm_countVec_model.sav"
        # model_file = open(model_name, "rb")
        # model = pickle.load(model_file)


        # article_text = response.get("data").get("comment")
        # article_predict_loaded_model = model.predict([article_text])


        f = open(os.getcwd()+"/machine_learning/model/aaa.txt", 'r')
        content = f.read()

        article_predict_loaded_model=True

        data = {
            "is_hoax": bool(article_predict_loaded_model),
            "curr_dir": model_name,
            "text": content
        }

        return data, 200
