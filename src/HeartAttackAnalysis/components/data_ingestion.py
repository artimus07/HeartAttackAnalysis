import os 
import urllib.request as request
from src.HeartAttackAnalysis.logging.logger import logging
from src.HeartAttackAnalysis.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion class with the given configuration.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the file from the specified URL in the configuration and stores it in the specified location.
        """
        # Ensure the root directory exists
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Construct the complete path for the local data file
        local_file_path = os.path.join(self.config.root_dir, self.config.local_data_file)

        # Download the file if it doesn't already exist
        if not os.path.exists(local_file_path):
            try:
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=local_file_path
                )
                logging.info(f"{filename} downloaded successfully with the following info:\n{headers}")
            except Exception as e:
                logging.error(f"Error occurred while downloading the file: {e}")
                raise e
        else:
            logging.info(f"File already exists at {local_file_path}")