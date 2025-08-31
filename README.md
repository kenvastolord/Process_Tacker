
# Process Monitor

A simple Python script that monitors active system processes and exports them to a JSON file.  
It also logs execution details and errors to a log file.

## 🧰 Features

- Retrieves active system processes using `ps aux`
- Parses and exports process data to `data/processes.json`
- Logs all activity to `logs/monitor.log`
- Provides console output for user feedback
- Handles common errors gracefully

## 📁 Project Structure

```

ProcessTracker/
├── monitor.py
├── logs/
│ └── monitor.log
└── data/
└── processes.json

```


## ⚙️ Requirements

- Python 3
- Unix-based system (Linux/macOS) — uses `ps` command via `subprocess`

No external libraries are required.

## 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the script:

```bash

python3 monitor.py

```

4. The script will:

- Log information to logs/monitor.log

- Export process data to data/processes.json

- Show status messages in the terminal

## 📝 Example Output

  JSON output (data/processes.json):

```bash

[
    {
        "USER": "root",
        "PID": "1",
        "CPU": "0.0",
        "MEM": "0.1",
        "COMMAND": "/sbin/init"
    },
    ...
]

```
