from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htm=browser.find_element_by_tag_name('html')
try:
    while True:
        htm.send_keys(Keys.UP)
        htm.send_keys(Keys.RIGHT)
        htm.send_keys(Keys.DOWN)
        htm.send_keys(Keys.LEFT)
except:
    print("game over")