# Ref https://gist.github.com/baijum/1047207/c670c7d1fe4a5a60d361d66869b20cc2ab1a4bf4
# https://www.youtube.com/watch?v=oM-yAjUGO-E

import unittest  #unittest is a python module for organizing test cases
import time
from selenium import webdriver    #It imports webdriver module from selenium library
from selenium.webdriver.common.keys import Keys   #keys module imported to execute keyboard keys
from selenium.webdriver.support.ui import WebDriverWait  # It makes the webpage to wait until fully loaded

class LoginTest(unittest.TestCase):  #TestCase class is inhereted from unittest
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.facebook.com')
        self.driver.maximize_window()

    # The testcase method always has to start with the word "test"
    def test_login(self):
        driver = self.driver
        #facebook_username = 'your email id'
        #facebook_password = 'your password'

        #email_Field_ID = 'email'
        #pass_Field_ID = 'pass'

        email_field = driver.find_element_by_id('email')
        email_field.clear()
        email_field.send_keys('subh.samal007@gmail.com')

        password_field = driver.find_element_by_id('pass')
        password_field.clear()
        password_field.send_keys('Samhis@facebook2017')

        login_button = driver.find_element_by_id('loginbutton')
        login_button.click()

        driver.get('https://www.facebook.com/subh.samal.712')

        status = driver.find_element_by_xpath("//div[@class='notranslate _5rpu']")
        time.sleep(5)
        #status.click()
        status.send_keys("I am learnign to automate facebook using selenium and python :) ...")

        time.sleep(20)

        post = driver.find_element_by_css_selector("button[data-testid='react-composer-post-button']")
        driver.execute_script("arguments[0].click();", post)
        #post.click()

if __name__ == "__main__":
    unittest.main()


# Future work: Use Xpath for username and password. Then improve it to reply and like to others post ###
