"""
Main module of the instagram-graph-api-job-job project.

"""

import logging

from ig_account import (
    get_account_info,
    get_day_account_metrics,
    get_lifetime_account_metrics,
)
from ig_media import (
    get_media_comments,
    get_media_id,
    get_media_info,
    get_media_metrics,
    get_stories_id,
    get_stories_metrics,
)
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
    ig_user_id = 17841411237972805
    base = "https://graph.facebook.com/v9.0"
    user_node = f"/{ig_user_id}"
    access_token = ""
    username = "vinicius.py"
    logger.info(f"GETTING DATA FROM INSTA USERNAME: {username}")

    logger.info(f"REQUESTING ACCOUNT DATA ...")
    account_info = get_account_info(base, user_node, access_token)
    logger.info(account_info)

    logger.info(f"REQUESTING DAILY METRICS ...")
    day_account_metrics = get_day_account_metrics(base, user_node, access_token)
    logger.info(day_account_metrics)

    logger.info(f"REQUESTING LIFETIME METRICS ...")
    lifetime_account_metrics = get_lifetime_account_metrics(
        base, user_node, access_token
    )
    logger.info(lifetime_account_metrics)

    logger.info(f"REQUESTING MEDIA DATA ...")
    media_ids = get_media_id(base, user_node, access_token)
    media_id_list = [media_id["id"] for media_id in media_ids["data"]]
    logger.info(media_id_list)

    media_info = get_media_info(base, media_id_list, access_token)
    logger.info(media_info)

    logger.info(f"REQUESTING MEDIA METRICS ...")
    media_metrics = get_media_metrics(base, media_id_list, access_token)
    logger.info(media_metrics)

    logger.info(f"REQUESTING MEDIA COMMENTS ...")
    media_comments = get_media_comments(base, media_id_list, access_token)
    comments_list = [comment["data"] for comment in media_comments]
    logger.info(comments_list)

    logger.info(f"REQUESTING STORIES METRICS ...")
    stories_ids = get_stories_id(base, user_node, access_token)
    logger.info(stories_ids)
    stories_id_list = [storie_id for storie_id in stories_ids["data"]]
    stories_metrics = get_stories_metrics(base, stories_id_list, access_token)
    logger.info(stories_metrics)

    logger.info("END OF JOB")
