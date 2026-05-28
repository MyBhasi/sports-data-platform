import json
import os
from datetime import datetime


class BronzeLoader:
    def __init__(self, base_path: str = "data/bronze"):
        self.base_path = base_path

    def save(self, data: dict, entity: str) -> str:
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        folder = os.path.join(self.base_path, entity)
        os.makedirs(folder, exist_ok=True)
        name = os.path.basename(entity)
        file_path = os.path.join(folder, f"{name}_{timestamp}.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

        for old_file in os.listdir(folder):
            old_path = os.path.join(folder, old_file)
            if old_path != file_path and old_file.endswith(".json"):
                os.remove(old_path)

        return file_path
