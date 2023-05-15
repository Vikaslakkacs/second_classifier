from secondClassifier.entity import DataIngestionConfig, PrepareBasemodelConfig
from secondClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from secondClassifier.utils import create_directory, read_yaml
from pathlib import Path




class ConfigurationManager:
    """Creating configuration data at each stage of project
    """
    def __init__(self, 
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)
        ##Creates directory for root directory
        create_directory(self.config.artifacts_root)
    
    def get_dataingestion_config(self)->DataIngestionConfig:
        """assign values to the data class DataIngestion

        Returns:
            DataIngestionConfig: Data ingestion data class
        """
        config_ingestion= self.config.data_ingestion
        ##Create directory
        create_directory(config_ingestion.root_dir)
        data_ingestion_config= DataIngestionConfig(
            root_dir= config_ingestion.root_dir,
            source_URL= config_ingestion.source_URL,
            local_data_file= config_ingestion.local_data_file,
            unzip_dir= config_ingestion.unzip_dir,
            clean_dir= config_ingestion.clean_dir
        )
        return data_ingestion_config
    def get_base_model_config(self)->PrepareBasemodelConfig:
        basemodel_details= self.config.prepare_base_model
        ##Create root directory for prepare basemodel

        
        base_model_config= PrepareBasemodelConfig(
            root_dir=Path(basemodel_details.root_dir),
            base_model_path=Path(basemodel_details.base_model_path),
            updated_model_path=Path(basemodel_details.updated_model_path),
            include_top=self.params.INCLUDE_TOP,
            image_size=self.params.IMAGE_SIZE,
            learning_rate=self.params.LEARNING_RATE,
            weights=self.params.WEIGHTS,
            classes=self.params.CLASSES
        )
        return base_model_config