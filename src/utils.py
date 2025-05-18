import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import pickle
from sklearn.metrics import mean_squared_error, r2_score


def save_object(file_path, obj):
    """
    Save the object to the specified file path using pickle.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Evaluate the models and return the model report.
    """
    try:
        report = {}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            report[model_name] = r2
        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    