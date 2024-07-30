import os
from pathlib import Path

list_of_files = [
    '.github/workflows/.gitkeep',  # GitHub Actions workflows configuration directory
    'src/__init__.py',  # Package initializer for the src directory
    'src/components/__init__.py',  # Package initializer for the components directory
    'src/components/data_ingestion.py',  # Data ingestion component
    'src/components/data_transformation.py',  # Data transformation component
    'src/components/model_trainer.py',  # Model training component
    'src/components/model_evolution.py',  # Model evaluation component
    'src/pipeline/__init__.py',  # Package initializer for the pipeline directory
    'src/pipeline/training_pipeline.py',  # Training pipeline script
    'src/pipeline/prediction_pipeline.py',  # Prediction pipeline script
    'src/utils/utils.py',  # Utility functions
    'src/logger/logging.py',  # Logging configuration
    'src/exception/exception.py',  # Custom exception handling
    'test/unit/__init__.py',  # Package initializer for the unit tests directory
    'test/integration/__init__.py',  # Package initializer for the integration tests directory
    'init_setup.sh',  # Initial setup script
    'requirements.txt',  # Project dependencies
    'requirements_dev.txt',  # Development dependencies
    'setup.py',  # Setup script for the project
    'setup.cfg',  # Configuration file for the setup script
    'pyproject.toml',  # Build system configuration
    'tox.ini',  # Tox configuration for testing
    'experiment/experiment.ipynb',  # Jupyter Notebook for experiments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    if filepath.suffix:  # Check if the path has a file extension (i.e., it's a file)
        filedir = filepath.parent
        os.makedirs(filedir, exist_ok=True)
        
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass  # create an empty file
    else:
        os.makedirs(filepath, exist_ok=True)
