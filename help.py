from pyautogui import * 
import pyautogui as pag
import time
import keyboard
import win32api, win32con
from keyboard import is_pressed as pre

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

with open("config.txt", "r") as f:
    inp = f.readlines()

xc = []
yc = []

for i,v in enumerate(inp):
    h = v.replace("\n","")
    h = h.split(",")
    xc.append(int(h[0]))
    yc.append(int(h[1]))
    
running = True
delay = 0.1

while running:
    if pre('0'):
        click(xc[0],yc[0])
        time.sleep(delay)
    if pre('1'):
        click(xc[1],yc[1])
        time.sleep(delay)  
    if pre('2'):
        click(xc[2],yc[2])
        time.sleep(delay)  
    if pre('3'):
        click(xc[3],yc[3])
        time.sleep(delay)
    if pre('4'):
        click(xc[4],yc[4])
        time.sleep(delay)
    if pre('5'):
        click(xc[5],yc[5])
        time.sleep(delay)
    if pre('6'):
        click(xc[6],yc[6])
        time.sleep(delay)
    if pre('7'):
        click(xc[7],yc[7])
        time.sleep(delay)
    if pre('8'):
        click(xc[8],yc[8])
        time.sleep(delay)
    if pre('9'):
        click(xc[9],yc[9])
        time.sleep(delay)
    if pre('enter'):
        click(xc[10],yc[10])
        time.sleep(delay)
    if pre('backspace'):
        click(xc[11],yc[11])
        time.sleep(delay)
    if pre('a'):
        running = False
        
print('Program ended')