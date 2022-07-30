import os
os.system('cls')

a = input("Do you want to install basic libraries for mouse movement? (y/n) >").lower()

if a in ["y","yes"]:
    os.system('py -m pip install -r reqs.txt')
    print('Installed basic libraries for mouse movement')
    os.system('cls')

a = input("""Do you want to install advanced libraries for image recognition (y/n)
For this you are required to install tesseract-ocr and put it into 
C:\ Program Files (x86)\ Tesseract-OCR\ tesseract
> """).lower()

if a in ["y","yes"]:
    os.system('py -m pip install -r requirements.txt')
    print('Installed advanced libraries for image recognition')
    os.system('cls')

a = input('Do you want to calibrate the porgram? >').lower()

if a in ["y","yes"]:
    os.system('py config.py')
    print('Calibrated the program')

print('done')