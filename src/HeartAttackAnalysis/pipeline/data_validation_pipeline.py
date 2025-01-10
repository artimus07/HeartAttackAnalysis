from src.HeartAttackAnalysis.config.configuration import DataValidationConfigurationManger
from src.HeartAttackAnalysis.components.data_validation import DataValidation
from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.exception.exception import HeartAttackAnalysisException

STAGE_NAME = 'Data Validation'

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            logging.info(f'>>>>>>>> stage {STAGE_NAME} started')
            data_validation_config = DataValidationConfigurationManger().get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
            logging.info(f'>>>>> stage {STAGE_NAME} completed')
        except HeartAttackAnalysisException as e:
            logging.error(f'An error occurred during data validation: {e}')
            raise e

if __name__ == '__main__':
    try:
        logging.info(f'>>>>>>>> stage {STAGE_NAME} started')
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logging.info(f'>>>>>>>> stage {STAGE_NAME} completed')
    except Exception as e:
        HeartAttackAnalysisException(e)