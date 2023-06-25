from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataIngestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeLin:
    def __init__(self) -> None:
        pass
    def ingestData(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_dataIngestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()