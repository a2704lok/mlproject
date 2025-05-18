import sys
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainer(self, train_array, test_array, preprocessd_path):
        try:
            logging.info("Splitting training and test data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            
            models = {
                "RandomForestRegressor": RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "LinearRegression": LinearRegression(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor()
            }
            
            model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, models)
            
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]
            best_model = models[best_model_name]
             
            if best_model_score < 0.6:
                raise Exception("No best model found with sufficient accuracy")
            
            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test, predicted)
            return r2
            
        except Exception as e:
            raise CustomException(e, sys)
            
        
        
