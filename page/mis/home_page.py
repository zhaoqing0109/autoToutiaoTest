from selenium.webdriver.common.by import By
from base.mis.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 信息管理菜单栏
        self.info_manage = (By.XPATH, "//*[text()='信息管理']")
        # 内容审核菜单栏
        self.content_manage = (By.XPATH, "//*[text()='内容审核']")

    def find_info_manage(self):
        return self.find_elt(self.info_manage)

    def find_content_manage(self):
        return self.find_elt(self.content_manage)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 信息管理菜单栏点击
    def click_info_manage(self):
        self.home_page.find_info_manage().click()

    # 内容审核菜单栏点击
    def click_content_manage(self):
        self.home_page.find_content_manage().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 跳转内容审核页面
    def to_aduit_page(self):
        # 点击信息管理菜单栏
        self.home_handle.click_info_manage()
        # 点击内容审核菜单栏
        self.home_handle.click_content_manage()