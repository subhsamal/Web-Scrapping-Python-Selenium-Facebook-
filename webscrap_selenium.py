# https://gist.github.com/baijum/1047207/c670c7d1fe4a5a60d361d66869b20cc2ab1a4bf4
#https://www.youtube.com/watch?v=oM-yAjUGO-E
#http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python
##########################################################################################
import time
from selenium import webdriver    #It imports webdriver module from selenium library
from selenium.webdriver.common.keys import Keys   #keys module imported to execute keyboard keys



driver = webdriver.Firefox()   #Firefox uses gekco driver which we already installed in the env path
#time.sleep(10)
#driver.quit()
driver.get('http://www.python.org')
assert "Python" in driver.title    # it asserts that python word is present in the title of that page

#Serach particular field on the page by name. In our case we will look for searchbox whihc has a name = "q"
element = driver.find_element_by_name("q")

element.clear()  #it will clear if any text is present in the searchbox
element.send_keys("pycon")  #send_keys is a method of keys module
element.send_keys(Keys.RETURN)

assert "No result found" not in driver.page_source

time.sleep(10)
driver.quit()
