import os
import pandas as pd 
from src.HeartAttackAnalysis.logging.logger import  logging
from src.HeartAttackAnalysis.exception.exception import HeartAttackAnalysisException
from src.HeartAttackAnalysis.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            # Read the data file into a DataFrame
            df = pd.read_csv(self.config.DATA_FILE)
            all_cols = set(df.columns)  # Use a set for faster lookups
            all_schema_keys = set(self.config.all_schema.keys())

            # Check if all columns in the data file are in the schema
            missing_columns = all_cols - all_schema_keys
            extra_columns = all_schema_keys - all_cols

            # Determine validation status
            validation_status = len(missing_columns) == 0 and len(extra_columns) == 0

            # Write validation status and details to the status file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}\n")
                if missing_columns:
                    f.write(f"Missing columns: {', '.join(missing_columns)}\n")
                if extra_columns:
                    f.write(f"Extra columns: {', '.join(extra_columns)}\n")

            return validation_status
        except Exception as e:
            raise HeartAttackAnalysisException(e)