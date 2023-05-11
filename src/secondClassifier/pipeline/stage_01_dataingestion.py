from secondClassifier.config.configuration import ConfigurationManager
from secondClassifier.components.dataingestion import dataIngestion



def main():
    ingestion_config= ConfigurationManager()
    data_ingestion_config= ingestion_config.get_dataingestion_config()
    dataingestion= dataIngestion(data_ingestion_config)
    dataingestion.download_data()
    dataingestion.unzip_dataset()
    dataingestion.cleanup_dataset()

if __name__=='__main__':
    main()
