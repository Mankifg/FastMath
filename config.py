from pyautogui import * 
import pyautogui as pag
import time
import keyboard
import win32api, win32con

inp = []

nums = ["0", "1","2","3","4","5","6","7","8","9","enter","delete", "top left corner of text apearing on screen","bottom right corner of text apearing on screen"]

for i in range(len(nums)):
    print(f'Press the {nums[i]} button.')
    keyboard.wait('space')
    pos = str(pag.position()[0]) + "," + str(pag.position()[1])
    inp.append(pos)

with open("config.txt", "w") as f:
    for i,v in enumerate(inp):
        f.write(v)
        f.write('\n')