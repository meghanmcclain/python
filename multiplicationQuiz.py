import pyinputplus as pyip
import random, time 

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions): #range() function starts at 0 by default and increments by 1 (default) and stops before specified # (numberOfQuestions, 10)
    num1 = random.randint(0, 9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handles by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes= ['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3) #3 tries, 8 seconds, ^%s$ = trim, get rid of white space
        # old school % formatting "shepher %s is %d years old" % (shepher, age)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(2) # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))