import os
import pandas as pd
import numpy as np
from src.ML_Project import logger
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import pickle
from src.ML_Project.entity.config_entity import DataTransformationConfig




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    """Note:- we can add any other data tranformations like Scaling, Encoding, PCA, etc..."""
 
    def transform(self, data: pd.DataFrame):
        num_cols = data.select_dtypes(include=["int64","float64"]).columns.tolist()
        cat_cols = data.select_dtypes(include=["object"]).columns.tolist()

        # initialize One-Hot-Encoder
        encoder = OneHotEncoder(
            drop="first",
            dtype="int64",
            sparse_output=False, 
            handle_unknown="ignore"
        )
        # Perform Encoding on Categorical-columns
        encoded_cat_cols = encoder.fit_transform(data[cat_cols])
        encoded_cat_cols_df = pd.DataFrame(encoded_cat_cols, columns=encoder.get_feature_names_out())
        transformed_data = pd.concat([encoded_cat_cols_df, data[num_cols]], axis=1)

        logger.info("Categorical columns of data encoded successfully!")

        # transform the "year" into "Car's-age" (age = current_year-year_of_car)
        current_year = 2025
        transformed_data["year"] = current_year - transformed_data["year"]
        transformed_data.rename(columns={"year":"age"}, inplace=True)
        
        logger.info("Year column transformed to Car's-Age")

        # save the OHE-encoder as pickle file
        with open("artifacts/data_transformation/OHE_encoder.pkl", "wb") as encoder_file_path:
            pickle.dump(encoder, encoder_file_path)
        logger.info("Saving OHE-encoder to pickle file at artifacts...")

        return transformed_data  


    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # transformations of data takes place before train-test split
        data = self.transform(data)
        
        # split the data into train & test sets (80%-20%)
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted dataset into training & test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)