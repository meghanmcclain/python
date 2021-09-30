# websiteURLs.py - Finds website urls beginning with http:// or https:// on the clipboard.
import pyperclip, re

text = str(pyperclip.paste())

websiteUrlRegex = re.compile(r'''
    https?://           #match http:// or https:// (the s is optional)
    (?:w{3}\.)?         #www-dot
    [a-zA-Z0-9_-]+      #domin name
    \.                  #dot
    [a-zA-Z]{2,4}       #extension
    ''', re.VERBOSE)

matches = []
for website in websiteUrlRegex.findall(text):
    matches.append(website)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No website urls starting with http:// or https:// found.')