import pyautogui
from PIL import Image, ImageGrab
import time
import keyboard
time.sleep(2)
basewidth = 100
img = Image.open('img\download.jpg')
img = img.convert('1')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth+basewidth,hsize), Image.ANTIALIAS)
data = img.load()
width, height = img.size
name="JNNCE"
count=0
file1=open("mark1_output.txt","w")
file1.write("\n")
for j in range(0, height):
    for k in range(0, width):
         if data[k,j] == 0:
            file1.write(name[count])
            count=count+1
         else:
            file1.write(" ")
         if count == len(name):
             count=0
    count=0
    file1.write("\n")
    print(j)
file1.close()          
