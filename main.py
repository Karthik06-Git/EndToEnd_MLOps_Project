from src.ML_Project import logger
from src.ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ML_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.ML_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.ML_Project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<< \n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<< \n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<< \n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed! <<<< \n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e