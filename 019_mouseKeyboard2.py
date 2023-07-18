import pyautogui as pag
import time as t

t.sleep(3)             # 잠깐 기다렸다 실행시키기 위해서

pag.click(255, 1757)   # 윈도우 찾기에서 클릭
t.sleep(0.5)

pag.typewrite('PowerPoint', interval=0.1) # 파워포인트를 입력하고
t.sleep(0.5)

pag.press('enter')     # 엔터키를 누른다

