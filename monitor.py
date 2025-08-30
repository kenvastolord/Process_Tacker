import logging
import os
import subprocess

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


logging.basicConfig(
    filename=os.path.join(log_dir, "monitor.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Starting logger successfully... ")


def get_active_processes():
    try:
        result = subprocess.run(
            ["ps", "aux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.returncode != 0:
            logging.error(f"Error getting processes: {result.stderr}")
            return []
        return result.stdout.splitlines()
    except Exception as e:
        logging.error(f"Exception occurred while retrieving processes: {str(e)}")
        return []
