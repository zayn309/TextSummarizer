from textSummarizer.constants import *
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.utils.common import read_yaml, create_directory

class ConfigurationManager:
    def __init__(self,
                 Config_filePath = CONFIG_FILE_PATH,
                 Params_filePath = PARAMS_FILE_PATH,):
        self.config = read_yaml(Config_filePath)
        self.params = read_yaml(Params_filePath)
        create_directory([self.config.artifacts_root])
        
    def get_dataIngestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        return data_ingestion_config