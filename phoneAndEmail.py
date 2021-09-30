# phoneAndEmail.py - Finds phone numbers & email addresses on the clipboard.
import pyperclip, re

text = str(pyperclip.paste())

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #group 1 - area code
    (\s|-|\.)?                          #group 2 - separater
    (\d{3})                             #group 3 - first 3 digits
    (\s|-|\.)                           #group 4 - separater
    (\d{4})                             #group 5 - last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #group 6 - extension (optional)
)''', re.VERBOSE)

#TODO: Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   #username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something
)''', re.VERBOSE)

#TODO: Find matches in clipboard text.
matches = [] #empty list
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #area code, first 3 digits, last 4 digits, and extension
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')