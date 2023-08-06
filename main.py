from pyautogui import *
import pyautogui as pag
import time
import keyboard
import win32api, win32con
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
)

with open("config.txt", "r") as f:
    inp1 = f.readlines()

h = inp1
inp1 = []

maxlen = 25

for i, v in enumerate(h):
    inp1.append(v.replace("\n", ""))

xc = []
yc = []
for i, v in enumerate(inp1):
    s = v.split(",")
    xc.append(int(s[0]))
    yc.append(int(s[1]))


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def clicksingle(n):
    click(xc[n], yc[n])


def clickW(num):
    num = str(num)
    for i in range(len(num)):
        clicksingle(int(num[i]))
        time.sleep(0.1)
    clicksingle(10)


def readimage(x, y, w, h):
    im1 = pag.screenshot(region=(x, y, w, h))
    im1.save(r"./image.png")

    image = "./image.png"
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    if len(text) > 0:
        text = text[0:-2]
        text = text.replace("x", "*")

    return text


tl = xc[12], yc[12]
br = xc[13], yc[13]

def solve(inp):
    try:
        rez = eval(inp)
        print(f'Solved {rez}')
        time.sleep(0.1)
        clickW(rez)
    except SyntaxError:
            pass
    except NameError:
            pass

while True:
    
    while True:
        inp = readimage(tl[0], tl[1], br[0] - tl[1], br[1] - tl[1])
        print(f"Len: {len(inp)}")
        if len(inp) < maxlen and len(inp) > 2:
            print(f"End len: {len(inp)}")
            break
    
    inp = inp.replace("€","6")

    if inp[-1] == "=":
        inp = inp[0:-1]


    print(f"solving {inp}")
    solve(inp)

    
    '''for i in range(len(inp) - 1):
        if inp[i] == "4" and inp[i + 1] == "+":
            try:
                inp = inp[::i] + inp[i + 1 :]
            except ValueError:
                pass'''
    
#bil sem tle

    
    
    