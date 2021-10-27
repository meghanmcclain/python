#! python3
#mapIt.py - Launches a map in the browser using an address from the
#command line or clipboard

import webbrowser, sys, pyperclip
#webbrowser opens browser to a specific page
#sys - reads the potential command line arguments
if len(sys.argv) > 1: #sys.argv var stores a list of the program's filename & command line arguments
    #Get address from command line
    address = ''.join(sys.argv[1:]).replace(" ", "+") #returns a single string value, chop off first element in array (program name)
else:
    #Get address from clipboard
    address = pyperclip.paste().replace(" ", "+")

webbrowser.open('https://www.google.com/maps/place/' + address) #to launch a web browser with the google maps url