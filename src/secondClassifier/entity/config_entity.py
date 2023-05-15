from dataclasses import dataclass
from pathlib import Path





##Data ingestion Entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    clean_dir: Path


##Preparing model data
@dataclass(frozen=True)
class PrepareBasemodelConfig:
    root_dir:Path
    base_model_path: Path
    updated_model_path: Path
    include_top: bool
    image_size: list
    learning_rate: float
    weights: str
    classes: int