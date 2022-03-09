import pyautogui, time

pyautogui.FAILSAFE = True
distance = 100

while pyautogui.FAILSAFE == True:
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    print('>>>Will Move mouse to right<<<')
    pyautogui.move(distance, 0, duration=0.2)
    time.sleep(30)
    print('>>>Will move mouse to left<<<')
    pyautogui.move(-distance, 0, duration=0.2)
    time.sleep(30)
