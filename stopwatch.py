#! python3
# stopwatch.py - A simple stopwatch program.
"""Using the time module and time.time() function
CTRL-C to get out of the infinite loop.
Using a KeyboardInterrupt exception to handle the Ctrl-C exception
When you press CTRL-C, instead of an error message displayin, Done is printed"""

import time

#Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctr-C to quit.')
input() #press Enter to begin
print('Started.')
startTime = time.time() #get the first lap's start time
lastTime = startTime
lapNum = 1

#TODO: Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')
