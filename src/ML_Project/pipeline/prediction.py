import pandas as pd
import numpy as np
from pathlib import Path
import joblib



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, data):
        prediction = self.model.predict(data)[0]

        return prediction
    

