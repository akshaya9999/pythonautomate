#since i use ubuntu i can't implement the getwindows() but i beleive the following is the code
import pyautogui,pyperclip

word=pyautogui.getWindowsWithTitle('LibreOfficeWriter')
word.activate()
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

content=pyperclip.paste()
print(content)