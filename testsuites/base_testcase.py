from selenium import webdriver
import unittest
import time
from Discuz.framework.browser_engine import BrowserEngine
browser=BrowserEngine()
class BaseTestcase(unittest.TestCase):
    def setUp(self):
        self.driver=browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def tearDown(self):
        time.sleep(5)
        self.driver =browser.quit_browser()
        # self.driver.close()

