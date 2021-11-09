from selenium import webdriver
import pyinputplus as pyip

browser = webdriver.Firefox()
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real-username_here')

passwordElem = browser.find_element_by_id('user_pass')

#method 1 : puts password in source code - AVOID
#passwordElem.send_keys('your_real_password_here')

#method 2 : prompts the user to enter their password - BETTER
response = pyip.inputStr('Please enter your password: ')
passwordElem.send_keys(response)

passwordElem.submit()