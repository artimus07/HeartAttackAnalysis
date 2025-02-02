from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.HeartAttackAnalysis.pipeline.data_validation_pipeline import DataValidationPipeline
from src.HeartAttackAnalysis.pipeline.data_transformation_pipeline import DataTransformationPipeline
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

STAGE_NAME = "Data Validation stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logging.info(f">>>>> stage {STAGE_NAME} completed")
except Exception as e:
    raise HeartAttackAnalysisException(e, sys)

STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logging.info(f">>>>> stage {STAGE_NAME} completed")

except Exception as e:
    raise HeartAttackAnalysisException(e, sys)