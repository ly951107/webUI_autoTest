from Discuz.testsuites.base_testcase import BaseTestcase
from Discuz.pageobjects.HomePage1 import testDiscuz1
from Discuz.pageobjects.HomePage3 import testDiscuz3
import unittest
import time
from Discuz.framework.logger import Logger
logger=Logger(logger="DiscuzTest3").getlog()
class DiscuzTest3(BaseTestcase):
    def test_discuz3(self):
        login4 = testDiscuz1(self.driver)
        login4.adminlogin("lxc","lxc960301.")
        login5=testDiscuz3(self.driver)
        title=login5.Select("haotest")
        try:
            self.assertEqual(title,"haotest",msg=title)
            logger.info("断言成功，搜索到haotest%s"%title)
        except:
            logger.error("断言错误")







