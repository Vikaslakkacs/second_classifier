from secondClassifier.config.configuration import ConfigurationManager
from secondClassifier.components.preparebasemodel import PrepareBaseModel



config= ConfigurationManager()
base_model_config= config.get_base_model_config()
prepare_base_model= PrepareBaseModel(base_model_config)
prepare_base_model.get_base_model()
prepare_base_model.update_base_model()
