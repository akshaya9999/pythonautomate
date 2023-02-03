import pyautogui
import time

while True:
    try:
        pyautogui.moveRel(10,0)
        pyautogui.moveRel(0,10)
        time.sleep(5)
    except KeyboardInterrupt:
        break
        
# print(pyautogui.position())
