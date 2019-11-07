'''

'''
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import current_app
from MNDT.db import get_db

class modeler:
    def __init__(self,app):
        self.df = pd.read_csv('./MNDT/static/model/earthquake1104.csv')
        self.df.drop(columns = 'Unnamed: 0',inplace = True)
        with app.app_context():
            self.db = get_db()

    def RFC(self):
        rfc_model = pickle.load(open('./MNDT/static/model/rndm_forest.sav', 'rb'))
        tvec = pickle.load(open('./MNDT/static/model/tvec.sav', 'rb'))
        X = self.df['text']
        X_vectorized = tvec.transform(X).todense()
        self.df['predicted_relavent'] = rfc_model.predict(X_vectorized)
        self.df.dropna(inplace = True)
        self.df['location'] = [
        str(ele).replace('\'','\"') for ele in self.df['location']
        ]
        self.df.to_sql(name = 'earthquake',con = self.db, if_exists = 'replace')
        self.db.commit()
