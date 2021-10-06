#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree completely. That sounds good to me.""",
        'busy': """I'm terribly sorry. Could we possibly do this later this week or next week?""",
        'morning': """Good morning. It is a beautiful day outside."""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT: #look in the TEXT dict for the key phrase, if it is in the dict
    pyperclip.copy(TEXT[keyphrase]) #get the value corresponding to that key and copy to clipboard
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)