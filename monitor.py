import logging
import os
from re import DEBUG

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


logging.basicConfig(
    filename=os.path.join(log_dir, "monitor.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Starting logger successfully... ")
