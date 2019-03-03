from selenium.webdriver.support.wait import WebDriverWait
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from Discuz.framework.logger import Logger
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):  #创建一个driver对象
        self.driver=driver
    def get(self,url):              #打开一个网页
        self.driver.get(url)
        logger.info("打开浏览器")
    def sendkeys(self,content,*loc):     #发送一个值
        try:
            e1 = self.driver.find_element(*loc)
            e1.send_keys(content)
            logger.info("%s页面%s元素发送成功"%(self,loc))
        except Exception as e:
            logger.error("%s页面%s元素发送失败"%(self,e))

    # def find_element(self,by_type,by_value):  #查找页面元素
        # if "by_type"=="by_name":
        #     self.driver.find_element_by_name("by_value")
        # if "by_type"=="by_xpath":
        #     self.driver.find_element_by_xpath("by_value")
        # if "by_type"=="by_css_selector":
        #     self.driver.find_element_by_css_selector("by_value")
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc))
            logger.info("页面%s元素查找成功"%(loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("%s页面元素未找到%s"%(loc))

    def click(self,*loc):   #进行一个点击操作
        try:
            el=self.driver.find_element(*loc)
            el.click()
            logger.info("点击成功%s"%el)
        except Exception as e:
            logger.error("点击失败%s"%e)
    def JiHuo(self,i):
        try:
            self.driver.switch_to.window(self.driver.window_handles[i])
            logger.info("激活窗口%s成功"%self)
        except Exception as e:
            logger.error("激活窗口%s失败"%e)
    def switch_to_iframe(self):
        try:
            self.driver.switch_to.frame(0)
            logger.info("查找iframe元素成功")
        except Exception as e:
            logger.error("查找iframe元素失败"%e)
    def HuoQuText(self,*loc):
        el=self.driver.find_element(*loc)
        return el.text
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("有屏幕截图bingq保存的路径是/screenshots/")
        except Exception as e:
            self.get_windows_img()
            logger.error("%s截屏失败"%e)

