"""Automate the Boring Stuff with Python
Manipulating mouse click and drag using GUI Automation
Create a Square Spiral"""

import pyautogui, time
time.sleep(5) #5 sec delay so can get mouse in right spot
pyautogui.click() #click to make the window active
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2) #Move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2) #Move down
    pyautogui.drag(-distance, 0, duration=0.2) #Move left
    distance = distance - change
    pyautogui.drag(0,-distance,duration=0.2) #Move Up
