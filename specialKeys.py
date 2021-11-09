from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.HOME) #scrolls to top
htmlElem.send_keys(Keys.END) #scrolls to bottom

# more commonly used keys in selenium.webdriver.common.keys module
""" htmlElem.send_keys(Keys.DOWN)
htmlElem.send_keys(Keys.UP)
htmlElem.send_keys(Keys.LEFT)
htmlElem.send_keys(Keys.RIGHT)

htmlElem.send_keys(Keys.ENTER)
htmlElem.send_keys(Keys.RETURN)

htmlElem.send_keys(Keys.PAGE_DOWN)
htmlElem.send_keys(Keys.PAGE_UP)

htmlElem.send_keys(Keys.F12)
htmlElem.send_keys(Keys.TAB) """
