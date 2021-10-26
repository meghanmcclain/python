#user always loses

import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program') #want to print log info

guess = None
while guess not in (1, 0):
    logging.debug('Start of guess')
    print('Guess the coin toss! Enter 1 for heads or 0 for tails:')
    guess = int(input())

logging.debug('Start of coin toss')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
    
logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?') 
   
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')