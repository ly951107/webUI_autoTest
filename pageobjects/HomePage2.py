from selenium.webdriver.common.by import By
from Discuz.pageobjects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time
# from Discuz.framework.logger import Logger
# logger=Logger(logger="testDiscuz2").getlog()
class testDiscuz2(BasePage):
    name_input = (By.NAME, "username")  # 用户姓名输入
    pwd_input = (By.NAME, "password")  # 用户密码输入
    login_btn = (By.CSS_SELECTOR, ".fastlg_l em")  # 登录按钮
    MoKuai = (By.CSS_SELECTOR, (".bm_c tr:nth-last-child(3) h2 a"))
    choose = (By.CSS_SELECTOR, ("tbody:nth-last-child(2) tr td:nth-child(2)"))  # 选中删除的对象
    delete = (By.LINK_TEXT, "删除")# 删除按钮
    QueRen = (By.NAME, "modsubmit")
    Center = (By.LINK_TEXT, "管理中心")  # 管理中心
    Center_pwd = (By.NAME, "admin_password")  # 管理中心密码
    Centersumbit = (By.CLASS_NAME, "btn")  # 管理中心提交
    LunTan = (By.CSS_SELECTOR, ".nav li:nth-child(7)")  # 点击论坛
    AddBanKuai = (By.CSS_SELECTOR, ".lastboard>a")  # 增加新板块
    BanKuaiName = (By.NAME, "newforum[1][]")  # 输入版块姓名
    BanKuaiSumbit = (By.CSS_SELECTOR, "#submit_editsubmit")  # 提交新建版块
    CenterLogout = (By.LINK_TEXT, "退出")  # 推出管理zhongxin
    GLLogout=(By.LINK_TEXT,"退出")
    FaTie = (By.NAME, "subject")
    Content = (By.CSS_SELECTOR, ".area textarea")  # 发帖内容
    FaTieButton = (By.CSS_SELECTOR, ".ptm .pn")
    #论坛实战二
    #  删除帖子

    def GLlogin(self,content1,content2):
        self.sendkeys(content1,*self.name_input)                                #输入用户名
        self.sendkeys(content2,*self.pwd_input)                                 #输入密码
        self.click(*self.login_btn)

    def Delete(self):
        time.sleep(3)
        self.click(*self.MoKuai)                                                #点击默认模块
        self.click(*self.choose)                                                #点击选中删除内容
        time.sleep(3)
        self.click(*self.delete)                                                #删除按钮
        self.click(*self.QueRen)                                                #确认删除
        time.sleep(5)
    # 创建新版块
    def build(self,CenterPwd):
        self.click(*self.Center)                                                #点击管理中心
        time.sleep(2)
        self.JiHuo(1)                                                           #激活新页面
        time.sleep(2)
        self.sendkeys(CenterPwd,*self.Center_pwd)                               #输入管理中心管理员密码
        time.sleep(2)
        self.click(*self.Centersumbit)                                          #点击提交
        time.sleep(2)
        self.JiHuo(1)
        self.click(*self.LunTan)                                               #点击论坛
        time.sleep(2)
        self.switch_to_iframe()
        self.click(*self.AddBanKuai)                                            #添加新模块
        time.sleep(2)
        # self.sendkeys(BanKuaiName,*self.BanKuaiName)                          #输入新模块名字
        self.click(*self.BanKuaiSumbit)                                         #点击提交
        self.click(*self.CenterLogout)                                          #管理中心退出
        self.JiHuo(0)
        time.sleep(3)
        self.click(*self.GLLogout)                                              #管理员退出登录

    #普通用户登录
    # def NewTie(self,content1,content2):
    #     # 1、普通用户登录
    #     time.sleep(3)
    #     self.sendkeys(content1, *self.FaTie)  # 发帖主题
    #     self.sendkeys(content2, *self.Content)  # 发帖内容
    #     self.click(*self.FaTieButton)           #点击发帖按钮







