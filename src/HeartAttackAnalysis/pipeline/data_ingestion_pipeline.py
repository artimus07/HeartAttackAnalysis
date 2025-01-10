from src.HeartAttackAnalysis.config.configuration import DataIngestionConfigurationManager
from src.HeartAttackAnalysis.components.data_ingestion import DataIngestion
from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.exception.exception import HeartAttackAnalysisException

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = DataIngestionConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    
    except Exception as e:
        HeartAttackAnalysisException(e)