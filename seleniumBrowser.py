from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://inventwithpython.com")

try:
    elem = browser.find_element_by_id('mce-EMAIL')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click() #follows the "Read Online for Free" link