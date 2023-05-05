# import pickle
import os

from flask_restful import Resource

######
from nltk.corpus import wordnet
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
import joblib
#######


class PredictionResource(Resource):
    
    def get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)
    
    def process_text(s):
        punctuation = string.punctuation+'‘'
        punctuation = punctuation + '’'
        nopunc = [char for char in s if char not in punctuation]
        nopunc = ''.join(nopunc)
        twitter = ['via', 'photo', 'rt', '@', '#', 'https']
        stopword = stop_words + twitter
        clean_string = [word.lower() for word in nopunc.split() if word.lower() not in stopword]
        clean_string = [lemmatizer.lemmatize(w, PredictionResource.get_wordnet_pos(w)) for w in clean_string]
        return clean_string

    def post(self):
        response = {
            "data": {
                "name": "JoJo",
                "comment": "Donald Trump is a beauty ambassador."
            }
        }

        model_name = os.getcwd()+"/machine_learning/models/svm_countVec_model.sav"
        # model_name = "svm_countVec_model.sav"
        loaded_model = joblib.load(model_name)
        # loaded_model.named_steps['bow'](analyzer=PredictionResource.process_text)

        article_text = response.get("data").get("comment")
        article_predict_loaded_model = loaded_model.predict([article_text])


        # f = open(os.getcwd()+"/machine_learning/model/aaa.txt", 'r')
        # content = f.read()

        # article_predict_loaded_model=True

        data = {
            "is_hoax": bool(article_predict_loaded_model[0]),
            "curr_dir": model_name
        }

        return data, 200
