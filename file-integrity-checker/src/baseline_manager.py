import json
from pathlib import Path

BASELINE_FILE = "baseline.json"

def save_baseline(data):

    with open(BASELINE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_baseline():

    if not Path(BASELINE_FILE).exists():

        raise FileNotFoundError(
            "Baseline file not found. Create a baseline first."
        )

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)