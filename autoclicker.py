"""
Created on Thu Sep 11 14:53:05 2025

@author: wailreiz
"""

import pyautogui
import time 

i = 0
while True:
    screenshot = pyautogui.screenshot()
    if (i == 0):
        pos = pyautogui.locateCenterOnScreen("vortexDownload.png")
        if pos:
            pyautogui.click(pos)
            i = 1
    else:
        pos = pyautogui.locateCenterOnScreen("slowDownload.png")
        if pos:
            pyautogui.click(pos)
            i = 0
    time.sleep(2)