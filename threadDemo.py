"""multithreading example in python
should print:
Start of program.
End of program.
Wake up!"""

import threading, time
print('Start of program.')

def takeANap(): 
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap) #Note: it's not takeANap() (it's not calling the function here)
threadObj.start() #second thread starts & ends

print('End of program.') #orignial thread terminates
