from src.HeartAttackAnalysis.constants import *
from src.HeartAttackAnalysis.utils.common import read_yaml, create_directories
from src.HeartAttackAnalysis.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, )

class DataIngestionConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,

        )
        return data_ingestion_config

class DataValidationConfigurationManger:
    def __init__(
            self, 
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH
    ):
        self.config_filepath = read_yaml(config_filepath)
        self.params_filepath = read_yaml(params_filepath)
        self.schema_filepath = read_yaml(schema_filepath)

        create_directories([self.config_filepath.artifacts_root])
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config_filepath.data_validation
        schema = self.schema_filepath.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            DATA_FILE= config.DATA_FILE,
            all_schema = schema,
        )

        return data_validation_config

class DataTransformationConfigurationManager:
    def __init__(
            self,
            config_file_path,
            params_filepath,
            schema_filepath,
            categorical_list,
            numerical_list,
    ):
        self.config_file_path = read_yaml(config_file_path)
        self.params_filepath = read_yaml(params_filepath)
        self.schema_filepath = read_yaml(schema_filepath)
        self.categorical_list = categorical_list
        self.numerical_list = numerical_list

        create_directories([self.config_file_path.artifacts_root])
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config_file_path.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            categorical_list= self.categorical_list,
            numerical_list=  self.numerical_list
        )

        return data_transformation_config