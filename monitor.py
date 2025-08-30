import json
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


def export_processes_to_json(processes, filename="data/processes.json"):
    try:
        processes_list = []
        for process in processes:
            process_details = process.split()
            process_dic = {
                "USER": process_details[0],
                "PID": process_details[1],
                "CPU": process_details[2],
                "MEM": process_details[3],
                "COMMAND": " ".join(process_details[10:]),
            }
            processes_list.append(process_dic)

        with open(filename, "a") as json_file:
            json.dump(processes_list, json_file, indent=2)

        logging.info(f"Processes data successfully exported to {filename}")

    except Exception as e:
        logging.error(f"Error exporting process data to JSON: {str(e)}")
