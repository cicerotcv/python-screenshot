from datetime import datetime
import os

from defaults import DEFAULT_PICTURES_DIR, DEFAULT_PROGRAM_DIR


class StoreManager:
    def __init__(self, context: str = None):
        self.context = context
        self.output_dir = self._get_output_dir()

    def _get_output_dir(self):
        output_dir = os.path.join(DEFAULT_PICTURES_DIR,
                                  DEFAULT_PROGRAM_DIR, self.context)
        return output_dir

    def get_filename(self):
        now = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        return now + ".png"

    def get_full_path(self, filename):
        return os.path.join(self.output_dir, filename)

    @staticmethod
    def ensure_dir_exists(path: str):
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"Path '{path}' created")
