from selenium.webdriver.common.by import By
from Discuz.pageobjects.BasePage import BasePage
import time
from Discuz.framework.logger import Logger
logger=Logger(logger="testDiscuz3").getlog()
class testDiscuz3(BasePage):
    Find = (By.NAME, "srchtxt")        #搜索文本框
    searchsubmit=(By.NAME,"searchsubmit")     #搜索提交按钮
    SameTie=(By.CSS_SELECTOR,".slst  li:nth-child(1) a")   #相似贴子的链接
    ChakanTitle=(By.CSS_SELECTOR,".ts span")
    def Select(self,content):
        time.sleep(2)
        self.sendkeys(content,*self.Find)
        logger.info("已输入haotest")
        self.click(*self.searchsubmit)
        logger.info("点击搜索")
        time.sleep(2)
        self.JiHuo(1)
        logger.info("激活窗口")
        time.sleep(2)
        self.click(*self.SameTie)
        logger.info("点击找到的haotest")
        self.JiHuo(2)
        title=self.HuoQuText(*self.ChakanTitle)
        # logger.info("查看")
        return title






