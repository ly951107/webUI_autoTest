from Discuz.testsuites.base_testcase import BaseTestcase
from Discuz.pageobjects.HomePage1 import testDiscuz1
from Discuz.pageobjects.HomePage4 import testDiscuz4
import unittest
import time
from Discuz.framework.logger import Logger
logger=Logger(logger="DiscuzTest4").getlog()
class DiscuzTest4(BaseTestcase):
    def test_discuz4(self):
        login6=testDiscuz1(self.driver)
        time.sleep(2)
        login6.adminlogin("lxc","lxc960301.")
        time.sleep(5)
        login6.defaultModule()
        time.sleep(3)
        login7=testDiscuz4(self.driver)
        login7.EditTieZi("num","one","two")
        login7.voteTieZi()




