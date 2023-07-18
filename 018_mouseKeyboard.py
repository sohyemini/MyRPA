import pyautogui
import time

print(f"screen size = {pyautogui.size()}")

while(True):
    # print(pyautogui.position().x, pyautogui.position().y)
    print(pyautogui.position())
    time.sleep(0.1)
