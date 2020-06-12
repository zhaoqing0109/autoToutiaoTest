# 后台管理系统登陆页面
import time

from selenium.webdriver.common.by import By
from utils import DriverUtils
from base.mis.base_page import BasePage, BaseHandle

# 对象库层
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # 账户名
        self.username = (By.NAME, "username")
        # 密码
        self.password = (By.NAME, "password")
        # 登陆按钮
        self.login_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, pwd):
        self.input_text(self.login_page.find_password(), pwd)

    # 点击登陆按钮
    def click_login_btn(self):
        # 定义好删除属性值的js脚本
        js = 'document.getElementById("inp1").removeAttribute("disabled")'
        # 执行js脚本
        DriverUtils.get_mis_driver().execute_script(js)
        # 点击登陆按钮
        time.sleep(2)
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登陆方法
    def test_mis_login(self, usr, pwd):
        # 输入用户名
        self.login_handle.input_username(usr)
        # 输入密码
        self.login_handle.input_password(pwd)
        # 点击登陆按钮
        self.login_handle.click_login_btn()
