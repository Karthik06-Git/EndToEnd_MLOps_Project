import os
import pandas as pd
from src.ML_Project import logger
from sklearn.model_selection import train_test_split
from src.ML_Project.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    """Note:- we can add any other data tranformations like Scaling, Encoding, PCA, etc..."""

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        # split the data into train & test sets (80%-20%)
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted dataset into training & test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)