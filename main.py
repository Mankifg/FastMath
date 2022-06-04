from pyautogui import * 
import pyautogui as pag
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

print('Go to the top left corner of the inp and press a')
keyboard.wait('a')
tl = [ pag.position()[0], pag.position()[1] ]
print('Go to the bottom right corner of the inp and press a')
keyboard.wait('a')
br = [ pag.position()[0], pag.position()[1] ]
print('config')



for i,v in enumerate(h):
    inp1.append(v.replace("\n",""))

xc = []
yc = []
for i,v in enumerate(inp1):
    s = v.split(",")
    xc.append(int(s[0]))
    yc.append(int(s[1]))
    
 

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
    im1 = pag.screenshot(region=(x,y,w,h))
    im1.save(r"./image.png")

    image = "./image.png"
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    if len(text) > 0:
        text = text[0:-2]
        text = text.replace("x","*")
        
    return text

def bfinp(x,y):
    
    click(x,y)
    click(x,y)
    click(x,y)
    
while True:
    if keyboard.press("q"):
        exit()
    inp = readimage(tl[0],tl[1],br[0] - tl[1],br[1] - tl[1])
    
    
    if len(inp) > 2:    
        for i in range(len(inp) - 1):
            if inp[i]== '4' and inp[i+1] == '+':
                inp = inp[::i] + inp[i+1:]
                        
    print(inp, end="")
    
    if "=" not in inp:
        try:
            rez = eval(inp)
            print(f"| {rez}")
            clickW(rez)
            time.sleep(0.5)
        except SyntaxError:
            pass
        except NameError:
            pass
        
    
