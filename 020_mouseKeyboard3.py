import pyautogui as pag
import time as t
import random

max_x = pag.size().width
max_y = pag.size().height

while(True):
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    pag.moveTo(x, y)
    print(x, y)
    t.sleep(5)