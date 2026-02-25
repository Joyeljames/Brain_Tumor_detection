import os
import urllib.request as request
import zipfile
from cnn_classification.utils.common import get_size
from cnn_classification import logger
from cnn_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def unzip_and_clean(self):
        """
        zip_file: str
        extracts the zip file into the unzip_dir and then deletes the zip file
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)