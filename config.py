from enum import Enum
import tomllib
from pathlib import Path

class Config:
    def __init__(self):
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)

            file_path = Path(config["settings"]["file_path"])
            if not file_path.exists():
                raise ValueError("Invalid file path.")

            self.file_path = file_path
            del file_path

            if config["settings"]["summary_frequency"]:
                if config["settings"]["summary_frequency"] < 1:
                    raise ValueError("Summary frequency must be greater than zero.")
                self.summary_frequency = config["settings"]["summary_frequency"]
            else:
                self.summary_frequency = 1

    def __str__(self):
        return f"Path: {self.file_path}\nSummary frequency: {self.summary_frequency}"

if __name__ == "__main__":
    cfg = Config()
    print(cfg)