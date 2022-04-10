import os
import pyautogui
from storemanager import StoreManager
from defaults import *
from utils import get_context


def main():

    context = get_context()

    screenshot = pyautogui.screenshot()

    sm = StoreManager(context)

    filename = sm.get_filename()
    full_path = sm.get_full_path(filename=filename)

    sm.ensure_dir_exists(sm.output_dir)

    screenshot.save(full_path)

    print(f"Screenshot saved at {full_path}")


if __name__ == '__main__':
    main()
