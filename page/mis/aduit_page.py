import time

from selenium.webdriver.common.by import By
from base.mis.base_page import BasePage, BaseHandle
from utils import select_option, DriverUtils


# 对象库层
class AduitPage(BasePage):
    def __init__(self):
        super().__init__()
        # 搜索文章输入框
        self.search_ar_box = (By.CSS_SELECTOR, "[placeholder*='输入: 文章']")
        # 状态选择栏
        # self.status_checkbox = ()
        # 结束时间
        self.end_time = (By.CSS_SELECTOR, "[placeholder*='结束']")
        # 查询按钮
        self.search_btn = (By.CSS_SELECTOR, ".find")
        # 审核通过按钮
        self.aduit_ok = (By.XPATH, "//*[text()='通过']")
        # 确定通过按钮
        self.submit_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 找到搜索文章名称输入框
    def find_shar_box(self):
        return self.find_elt(self.search_ar_box)

    # 搜索条件栏：结束时间
    def find_end_time(self):
        return self.find_elt(self.end_time)

    # 搜索按钮
    def find_sh_btn(self):
        return self.find_elt(self.search_btn)

    # 审核通过按钮
    def find_ad_ok(self):
        return self.find_elt(self.aduit_ok)

    # 确定审核通过按钮
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


# 操作层
class AduitHandle(BaseHandle):
    def __init__(self):
        self.ad_page = AduitPage()

    # 输入文章名称搜索条件
    def input_sr_aritcal(self, text):
        self.input_text(self.ad_page.find_shar_box(), text)

    # 选择过滤文章的状态
    def check_ar_status(self, status):
        # 调用公用下拉框选择的函数
        select_option(DriverUtils.get_mis_driver(), "请选择状态", status)

    # 清除文章发表结束时间
    def clear_end_time(self):
        self.ad_page.find_end_time().clear()

    # 查询按钮的点击
    def click_query_btn(self):
        self.ad_page.find_sh_btn().click()

    # 通过按钮的点击
    def click_ps_btn(self):
        self.ad_page.find_ad_ok().click()

    # 确定按钮的点击
    def click_sb_btn(self):
        self.ad_page.find_submit_btn().click()


# 业务层
class AduitProxy:
    def __init__(self):
        self.ad_handle = AduitHandle()

    # 审核文章的方法
    def test_aduit_aritcal(self, title):
        # 1.输入文章名称
        self.ad_handle.input_sr_aritcal(title)
        # 2.选择待审核
        self.ad_handle.check_ar_status("待审核")
        # 3.清空结束时间
        time.sleep(2)
        self.ad_handle.clear_end_time()
        # 4.点击查询按钮
        self.ad_handle.click_query_btn()
        # 5.点击文章的通过按钮
        time.sleep(2)
        self.ad_handle.click_ps_btn()
        time.sleep(2)
        # 6.点击确认通过按钮
        self.ad_handle.click_sb_btn()
        time.sleep(2)
        # 7.选择审核通过
        self.ad_handle.check_ar_status("审核通过")
        time.sleep(2)
        # 8.点击查询
        self.ad_handle.click_query_btn()
        time.sleep(2)
