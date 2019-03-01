from selenium.webdriver.common.by import By
from Discuz.pageobjects.BasePage import BasePage
import time
class testDiscuz1(BasePage):
    #定位各个元素
    name_input = (By.NAME, "username")                                              #用户姓名输入
    pwd_input= (By.NAME, "password")                        #用户密码输入
    login_btn=(By.CSS_SELECTOR,".fastlg_l em")              #登录按钮
    default_module = (By.CSS_SELECTOR, (".bm_c tr:nth-child(2) h2 a"))              #默认模块
    post = (By.NAME, "subject")                              #发帖
    post_content = (By.CSS_SELECTOR, ".area textarea")           # 发帖内容
    post_btn = (By.CSS_SELECTOR, ".ptm .pn")             #发表帖子按钮
    reply_text =(By.CSS_SELECTOR,".pt")                     #回复框
    reply_post =(By.CSS_SELECTOR,".ptm .pn strong")      #回复帖子
    logout=(By.LINK_TEXT,"退出")                          #退出登录
    new_module = (By.CSS_SELECTOR,"tr:nth-child(2) td h2 a")  # 新模块
    #论坛实站1   # 用户登录
    def adminlogin(self,content1,content2):
        self.sendkeys(content1,*self.name_input)            #输入用户名
        self.sendkeys(content2,*self.pwd_input)             #输入密码
        self.click(*self.login_btn)                         #点击登陆按钮
    def defaultModule(self):                                #点击登录默认模块
        self.click(*self.default_module)
    def NewBanKuai(self):                                   #点击登录新模块
        time.sleep(3)
        self.click(*self.new_module)
    #用户发贴
    def faTie(self,content1,content2):
        self.sendkeys(content1,*self.post)             #发帖主题
        self.sendkeys(content2,*self.post_content)           #发帖内容
        self.click(*self.post_btn)                   #发帖按钮
    #用户回复
    def HuiFu(self,content3):
        self.sendkeys(content3,*self.reply_text)        # 回复框
        time.sleep(5)
        self.click(*self.reply_post)                    #回复按钮

    #用户退出
    def Logout(self):
        self.click(*self.logout)

















