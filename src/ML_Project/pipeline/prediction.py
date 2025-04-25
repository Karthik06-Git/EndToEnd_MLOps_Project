import pandas as pd
import numpy as np
import pickle as pk
from sklearn.preprocessing import OneHotEncoder
from pathlib import Path
from src.ML_Project import logger
import joblib



class PredictionPipeline:
    def __init__(self):
        # Load the Model
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        # Load the Target-Std-scaler
        with open("artifacts/data_transformation/target_std_scaler.pkl", "rb") as scaler_file_path:
            self.target_scaler = pk.load(scaler_file_path)


    def transform_data(self, data):
        # transform the "year" into "Car's-age" (age = current_year  - year_of_purchase)
        current_year = 2025
        data["year"] = current_year - data["year"]
        data.rename(columns={"year":"age"}, inplace=True)

        num_cols = data.select_dtypes(include=["int64","float64"]).columns.tolist()
        cat_cols = data.select_dtypes(include=["object"]).columns.tolist()

        # Load the saved Std-scaler for features
        with open("artifacts/data_transformation/features_std_scaler.pkl", "rb") as scaler_file_path:
            scaler = pk.load(scaler_file_path)
        # Perform Scaling on Numerical-columns 
        data[num_cols] = scaler.transform(data[num_cols])

        # initialize One-Hot-Encoder
        encoder = OneHotEncoder(
            drop="first",
            dtype="int64",
            sparse_output=False, 
            handle_unknown="ignore"
        )
        # Perform Encoding on Categorical-columns
        train_data = pd.read_csv("artifacts/data_ingestion/Car_Selling_Prices_data.csv")
        encoder.fit_transform(train_data[cat_cols])
        encoded_cat_cols = encoder.transform(data[cat_cols])
        encoded_cat_cols_df = pd.DataFrame(encoded_cat_cols, columns=encoder.get_feature_names_out())

        transformed_data = pd.concat([encoded_cat_cols_df, data[num_cols]], axis=1)
        
        logger.info("Input data transformed acc to model requirement")
        return transformed_data
    


    def predict(self, input_data):
        transformed_data = self.transform_data(input_data)
        prediction = self.model.predict(transformed_data)[0]
        prediction = np.reshape(prediction, (-1,1))
        # rescale the output price to normal range
        prediction = self.target_scaler.inverse_transform(prediction)[0][0]

        return prediction
    

