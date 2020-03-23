import cv2
import numpy as np
import pyautogui
import  time
count = 0
while count<5:
    count = count + 1
    name = str(count)+"screenshot.jpg"
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
    cv2.imwrite(name,img)
    time.sleep(3)
    
