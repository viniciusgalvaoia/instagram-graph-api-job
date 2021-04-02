"""
Main module of the instagram-graph-api-job-job project.

"""

import logging
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
    logger.info("STARTING JOB")

    logger.info("END OF JOB")
