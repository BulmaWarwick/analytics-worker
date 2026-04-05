import os
import json
import logging
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Utils:
    def __init__(self):
        self.config_file = 'analytics-worker/config.json'

    def load_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get_config(self):
        return self.load_config()

    def get_config_path(self):
        return os.path.join(os.path.dirname(__file__), 'config.json')

    def save_config(self, data: Dict):
        with open(self.get_config_path(), 'w') as f:
            json.dump(data, f, indent=4)