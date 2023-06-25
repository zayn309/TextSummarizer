from textSummarizer.logging import logger
from textSummarizer.pipeLine.stage_01_data_ingestion import DataIngestionTrainingPipeLin
from textSummarizer.logging import logger

STATGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> {STATGE_NAME} Started <<<<<<<")
    dataIngestion = DataIngestionTrainingPipeLin()
    dataIngestion.ingestData()
    logger.info(f">>>>>> {STATGE_NAME} Completed <<<<<<<")
except Exception as e:
    raise e