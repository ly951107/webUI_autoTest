from Discuz.testsuites.base_testcase import BaseTestcase
from Discuz.pageobjects.HomePage1 import testDiscuz1
import unittest
import time
from Discuz.framework.logger import Logger
logger=Logger(logger="DiscuzTest1").getlog()

class DiscuzTest1(BaseTestcase):
    def test_discuz1(self):
        login1=testDiscuz1(self.driver)
        time.sleep(1)
        name=login1.adminlogin("lxc","lxc960301.")
        # name = login1.adminlogin("admin", "ly951107")
        try:
            self.assertEqual(name,"lxc",msg=name)
            logger.info("用户名%s登陆成功"%name)
        except:
            logger.error("用户名%s登录失败"%name)

        time.sleep(1)
        default_module=login1.defaultModule()
        try:
            self.assertEqual(default_module,"默认模块",msg=default_module)
            logger.info("成功进入默认模块")
        except:
            logger.error("未进入默认模块")
        login1.faTie("猪猪女孩2","小可爱小可爱小可爱小可爱")
        # try:
        #     self.assertEqual(post_assert,"猪猪女孩2",msg=post_assert)
        #     logger.info("成功发帖")
        # except:
        #     logger.error("未成功发帖")
        time.sleep(16)
        login1.HuiFu("小仙女小仙女小仙女小仙女")
        # try:
        #     self.assertEqual(reply_post_assert,"小仙女小仙女小仙女小仙女",msg=reply_post_assert)
        #     logger.info("成功回复帖子")
        # except:
        #     logger.error("未成功回复帖子")
        time.sleep(1)
        login1.Logout()
        # try:
        #     self.assertEqual(logout_assert,"退出",msg=logout_assert)
        #     logger.info("用户成功退出")
        # except:
        #     logger.error("用户未成功退出")
# if __name__=="__main__":
#     unittest.main()