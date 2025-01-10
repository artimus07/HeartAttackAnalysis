import os
from src.HeartAttackAnalysis.logging.logger import  logging
from src.HeartAttackAnalysis.exception.exception import  HeartAttackAnalysisException
from src.HeartAttackAnalysis.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.scaler = StandardScaler()

    def scale_numerical_data(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Enter the scale_numerical_data in DataTransformation class")
        scaled_array = self.scaler.fit_transform(df[self.config.numerical_list[:-1]])
        scaled_df = pd.DataFrame(scaled_array, columns=self.config.numerical_list[:-1])
        return scaled_df

    
    def add_target_column(self, scaled_df: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Enter the add_target_column in DataTransformation class")
        scaled_df["target"] = df["target"]
        return scaled_df
    
    def melt_data(self, df:pd.DataFrame)->pd.DataFrame:
        logging.info("Enter the melt_data in DataTransformation class")
        return pd.melt(df, id_vars= "target", var_name = "features", value_name = "value")
    
    def detect_and_remove_outliers(self, df: pd.DataFrame, numerical_list: list, multiplier: float = 2.5) -> pd.DataFrame:
        logging.info("Enter the detect_and_remove_outliers in DataTransformation class")

        def calculate_iqr_bounds(series, multiplier):
            Q1 = np.percentile(series, 25)
            Q3 = np.percentile(series, 75)
            IQR = Q3 - Q1
            lower_bound = Q1 - (multiplier * IQR)
            upper_bound = Q3 + (multiplier * IQR)
            return lower_bound, upper_bound

        for col in numerical_list:
            lower_bound, upper_bound = calculate_iqr_bounds(df[col], multiplier)
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        return df
    
    def encode_categorical_data(self, df:pd.DataFrame)->pd.DataFrame:
        logging.info("Enter the encode_categorical_data in DataTransformation class")
        return pd.get_dummies(df, columns = self.config.categorical_list[:-1])
    
    def split_data(self, df: pd.DataFrame) -> tuple:
        """Splits the data into training and testing sets and saves them as CSV files."""
        X = df.drop(["target"], axis=1)
        y = df["target"]

        X[self.config.numerical_list[:-1]] = self.scaler.fit_transform(X[self.config.numerical_list[:-1]])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=3)

        train_dir = Path(self.config.root_dir) / "train"
        test_dir = Path(self.config.root_dir) / "test"

        train_dir.mkdir(parents=True, exist_ok=True)
        test_dir.mkdir(parents=True, exist_ok=True)

        X_train.to_csv(train_dir / "X_train.csv", index=False)
        X_test.to_csv(test_dir / "X_test.csv", index=False)
        y_train.to_csv(train_dir / "y_train.csv", index=False)
        y_test.to_csv(test_dir / "y_test.csv", index=False)

        print(f"X_train: {X_train.shape}")
        print(f"X_test: {X_test.shape}")
        print(f"y_train: {y_train.shape}")
        print(f"y_test: {y_test.shape}")

        return X_train, X_test, y_train, y_test
    
    
        