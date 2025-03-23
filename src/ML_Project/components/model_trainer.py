import os
import pandas as pd
import warnings
from src.ML_Project import logger
from sklearn.linear_model import ElasticNet
import joblib

from src.ML_Project.entity.config_entity import ModelTrainerConfig




class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        X_train = train_data.drop([self.config.target_column], axis=1)
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]] 
        y_test = test_data[[self.config.target_column]]

        # define the model
        lr_model = ElasticNet(
            alpha= self.config.alpha,
            l1_ratio= self.config.l1_ratio,
            random_state= 42
        )
        
        # train the model
        lr_model.fit(X_train, y_train)

        warnings.filterwarnings("ignore")
        
        # save the model
        joblib.dump(lr_model, os.path.join(self.config.root_dir, self.config.model_name))