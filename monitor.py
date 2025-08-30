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

print("Starting process monitor...")
logging.info(" Logger started successfully... ")


def get_active_processes():
    try:
        result = subprocess.run(
            ["ps", "aux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output = result.stdout.strip()

        if not output:
            print("Warning: 'ps aux' returned no data. ")
            logging.warning("No output received from 'ps aux'. ")
            return []

        return output.splitlines()

    except subprocess.CalledProcessError as e:
        logging.error(f"'ps aux' command failed with code {e.returncode}: {e.stderr}")
        print("Error: Failed to retrieve process list. Check logs.")
        return []

    except FileNotFoundError:
        logging.error("The 'ps' command is not found on this system.")
        print("Error: 'ps' command not available")
        return []

    except Exception as e:
        logging.error(f"Unexpected error while retrieving processes: {str(e)}")
        print("An unexpected error occurred while retrieving processes.")
        return []


def export_processes_to_json(processes, filename="data/processes.json"):
    try:
        if not processes:
            print("Warning: No processes to export")
            logging.warning("No processes to export")

        process_list = []
        for process in processes[1:]:
            process_details = process.split()

            if len(process_details) < 11:
                logging.warning("Skip a malformed process line.")
                continue

            process_dic = {
                "USER": process_details[0],
                "PID": process_details[1],
                "CPU": process_details[2],
                "MEM": process_details[3],
                "COMMAND": " ".join(process_details[10:]),
            }
            process_list.append(process_dic)

        if not process_list:
            logging.warning("No valid processes to export after parsing.")
            print("Warning: No valid processes to export.")
            return

        data_dir = os.path.dirname(filename)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        with open(filename, "a") as json_file:
            json.dump(process_list, json_file, indent=2)

        print("Export completed successfully.")
        logging.info(f"Process data successfully exported to {filename}")

    except PermissionError:
        logging.error(f"Permission denieded: cannot write to {filename}")
        print(f"Error: cannot write to {filename} (permission denieded)")

    except Exception as e:
        print("An error occurred while exporting the process data. Check the logs.")
        logging.error(f"Error exporting process data to JSON: {str(e)}")

    finally:
        print("Export function finished.")


if __name__ == "__main__":
    processes = get_active_processes()
    export_processes_to_json(processes)
