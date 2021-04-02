"""
Main module of the monthly-bi-python-job project. ETL to create the MaterialRevenue table:

*   format_query formats the query, adding the year and month from the date
*   execute_query, from utils, executes the query in athena and stores the table in a dataframe
*   format_folder_path formats the folder path where table will be saved
*   write_to_s3 sends the dataframe as parquet file to formatted bucket at s3
"""

import logging
import os
from datetime import datetime

import awswrangler as wr
import boto3
import pandas as pd
from rich.logging import RichHandler
from rich.traceback import install


FORMAT = "[%(levelname)s] [%(message)s]"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%Y-%m-%d %H:%M:%S]",
    handlers=[RichHandler(show_level=False, show_path=False)],
)
install()
logger = logging.getLogger("main")


if __name__ == "__main__":
    # logging info
    logger.info(f"date: ")

    logger.info("END OF JOB")
