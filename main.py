from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

with open("config.txt", "r") as f:
    inp1 = f.readlines()
    
h = inp1
inp1 = []
print(h)
for i,v in enumerate(h):
    inp1.append(v.replace("\n",""))

xc = []
yc = []
for i,v in enumerate(inp1):
    s = v.split(",")
    xc.append(int(s[0]))
    yc.append(int(s[1]))
    
print(xc)
print(yc)   

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clicksingle(n):
    click(xc[n],yc[n])
    
    
def clickW(num):
    num = str(num)
    for i in range(len(num)):
        clicksingle(int(num[i]))
    clicksingle(10)
    
def readimage(x,y,w,h):
    im1 = pyautogui.screenshot(region=(x,y,w,h))
    im1.save(r"./savedimage.png")

    image = "./savedimage.png"
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    if len(text) > 0:
        text = text[0:-2]
        inp = text.replace("x","*")
        
    return text

def bfinp(x,y):
    
    click(x,y)
    click(x,y)
    click(x,y)
    
while True:
    if keyboard.press("q"):
        exit()
    inp = readimage(150,280,1000,75)
    
    
    if len(inp) > 1:    
        if inp[1] == "4":
            if len(inp) > 2:
                inp = inp[0] + inp[2:]  
                
    print(inp, end="")
    
    if "=" not in inp:
        try:
            rez = eval(inp)
            print(f"| {rez}")
            clickW(rez)
        except SyntaxError:
            pass
        except NameError:
            pass
    
