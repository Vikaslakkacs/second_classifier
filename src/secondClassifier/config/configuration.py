from secondClassifier.entity import DataIngestionConfig
from secondClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from secondClassifier.utils import create_directory, read_yaml





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