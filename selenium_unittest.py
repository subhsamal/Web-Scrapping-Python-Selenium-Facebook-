# https://gist.github.com/baijum/1047207/c670c7d1fe4a5a60d361d66869b20cc2ab1a4bf4
# https://www.youtube.com/watch?v=oM-yAjUGO-E

# Read about unittest module https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/pythons-unit-test-framework/
# https://www.obeythetestinggoat.com/book/chapter_02_unittest.html
# https://pymotw.com/2/unittest/

import unittest  #unittest is a python module for organizing test cases
import time
from selenium import webdriver    #It imports webdriver module from selenium library
from selenium.webdriver.common.keys import Keys   #keys module imported to execute keyboard keys

#Inheret a python class from unittest.TestCase class
class PythonOrgSearch(unittest.TestCase):
#The setUp is part of initialization, this method will get called before every test function which you are going to write in this test case class.
    def setUp(self):
        self.driver = webdriver.Firefox()



# This is the test case method. The first line inside this method create a local reference to the driver object created in setUp method.
# The testcase method always has to start with the word "test"
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://python.org")
        self.assertIn("Python", driver.title)
        element = driver.find_element_by_name("q")
        element.send_keys("pycon")
        element.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_source

    def tearDown(self):
        self.driver.quit()

# boiler plate code to run the test suite:
if __name__ == "__main__":
    unittest.main()
