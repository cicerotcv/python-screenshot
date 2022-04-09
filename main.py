import os
import pyautogui
from datetime import datetime


DEFAULT_HOME_DIR = os.environ['USERPROFILE']
DEFAULT_PICTURES_DIR = os.path.join(DEFAULT_HOME_DIR, "Pictures")
DEFAULT_OUTPUT_DIR = os.path.join(DEFAULT_PICTURES_DIR, 'python-screenshot')


def ensure_dir_exists(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"PATH: '{path}' created")


def get_filename():
    now = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    return now + ".png"


def main():
    screenshot = pyautogui.screenshot()

    filename = get_filename()
    full_path = os.path.join(DEFAULT_OUTPUT_DIR, filename)
    ensure_dir_exists(DEFAULT_OUTPUT_DIR)

    screenshot.save(full_path)

    print(f"Screenshot saved at {full_path}")


if __name__ == '__main__':
    main()
