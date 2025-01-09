from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.HeartAttackAnalysis.exception.exception import HeartAttackAnalysisException
import sys

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logging.info(f">>>>> stage {STAGE_NAME} completed")

except Exception as e:
    raise HeartAttackAnalysisException(e, sys)