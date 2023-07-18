import pyautogui as pag

printscr = pag.screenshot()
printscr.save(r".\files\printscr.png")

pag.screenshot(r".\files\printerscr2.png")

pag.screenshot(r".\files\screenshot.png", region=(100, 100, 400, 400))

