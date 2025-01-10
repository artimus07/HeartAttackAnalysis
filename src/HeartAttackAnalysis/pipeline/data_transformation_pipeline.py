from src.HeartAttackAnalysis.config.configuration import DataTransformationConfigurationManager
from src.HeartAttackAnalysis.components.data_transformaton import DataTransformation
from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.exception.exception import HeartAttackAnalysisException
import pandas as pd
from src.HeartAttackAnalysis.constants import *

STAGE_NAME = 'Data Transformation'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            logging.info(f'>>>>>>>> stage {STAGE_NAME} started')
            config = DataTransformationConfigurationManager(
                config_file_path=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH,
                schema_filepath=SCHEMA_FILE_PATH,
                categorical_list=["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "target"],
                numerical_list=['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target']
            )

            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            df = pd.read_csv(data_transformation_config.data_path)
            outlier_removed_df = data_transformation.detect_and_remove_outliers(df, config.numerical_list[:-1])
            scaled_df = data_transformation.scale_numerical_data(outlier_removed_df)
            scaled_with_target_df = data_transformation.add_target_column(scaled_df, outlier_removed_df)
            
            # Ensure categorical columns are included before encoding
            combined_df = pd.concat([scaled_with_target_df, outlier_removed_df[config.categorical_list[:-1]]], axis=1)
            
            encoded_df = data_transformation.encode_categorical_data(combined_df)
            data_transformation.split_data(encoded_df)
            logging.info(f'>>>>> stage {STAGE_NAME} completed')
        except HeartAttackAnalysisException as e:
            logging.error(f'An error occurred during data transformation: {e}')
            raise e
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')
            raise HeartAttackAnalysisException(e)

if __name__ == '__main__':
    try:
        logging.info(f'>>>>>>>> stage {STAGE_NAME} started')
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logging.info(f'>>>>>>>> stage {STAGE_NAME} completed')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise HeartAttackAnalysisException(e)