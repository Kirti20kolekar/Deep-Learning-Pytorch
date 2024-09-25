import sys
import os

# Add the path to the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Initialize data ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        logging.info(f"Data ingestion completed successfully.")
        logging.info(f"Training data stored at: {train_data_path}")
        logging.info(f"Test data stored at: {test_data_path}")

    except CustomException as e:
        logging.error(f"An error occurred during data ingestion: {str(e)}")
        raise e

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise CustomException(e, sys)
