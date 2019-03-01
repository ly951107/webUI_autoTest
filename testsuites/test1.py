from Discuz.testsuites.base_testcase import BaseTestcase
from Discuz.pageobjects.HomePage1 import testDiscuz1
import unittest
import time

class DiscuzTest1(BaseTestcase):
    def test_discuz1(self):
        login1=testDiscuz1(self.driver)
        time.sleep(1)
        login1.adminlogin("lxc","lxc960301.")
        time.sleep(1)
        login1.defaultModule()
        login1.faTie("猪猪女孩2","小可爱小可爱小可爱小可爱")
        time.sleep(16)
        login1.HuiFu("小仙女小仙女小仙女小仙女")
        time.sleep(1)
        login1.Logout()
if __name__=="__main__":
    unittest.main()