import os
from urllib import request
import tarfile
from secondClassifier.config.configuration import DataIngestionConfig
from pathlib import Path






class dataIngestion:
    """Performing Data ingestion process
    1. Retrieving the data from url
    2. unzipping the data
    3. cleaning up the data (if required.)
    """
    def __init__(self, config:DataIngestionConfig):
        """Define configuration details of data ingestion"""
        self.config= config

    def download_data(self):
        """Retrieves the data from url and downloads to specific folder."""
        ##Checking if data set file already exits else download
        if not os.path.exists(self.config.local_data_file):
            request.urlretrieve(self.config.source_URL,
                                filename=self.config.local_data_file)

    def unzip_dataset(self):
        """Un zips the dataset from tgz
        """
        if  os.path.exists(self.config.local_data_file) and not os.path.exists(self.config.clean_dir):
            with tarfile.open(self.config.local_data_file) as dsf:
                dsf.extractall(self.config.unzip_dir)
        
    def cleanup_dataset(self):
        """Cleansup the data set apart from actual data
        """
        ##Cleaning un necessary files. till now we have only one file
        ## loop around the folder and delete files which are not in folder
        for file_folder in os.listdir(self.config.clean_dir):
            ## if there is no suffix for the file it is a folder
            if Path(file_folder).suffix!='':
                os.remove(os.path.join(self.config.clean_dir, file_folder))
        
    