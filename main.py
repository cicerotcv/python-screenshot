import functools

import keyboard
import pyautogui

from storemanager import StoreManager
from utils import get_context


def screenshot(sm):
    screenshot = pyautogui.screenshot()

    filename = sm.get_filename()
    full_path = sm.get_full_path(filename=filename)

    sm.ensure_dir_exists(sm.output_dir)

    screenshot.save(full_path)
    print(f"Screenshot saved at {full_path}")


def main():
    try:
        context = get_context()
        if context:
            print(f"Started with context: '{context}'")

        sm = StoreManager(context)

        callback = functools.partial(screenshot, sm)
        keyboard.add_hotkey('ctrl+alt+enter', callback)
        keyboard.wait()

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
