from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtils


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 滑动区域的元素
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        # 频道
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        # 第一条文章
        self.first_artical = (By.XPATH, "//*[contains(@text,'评论')]")

    # 找滑动的区域的元素
    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    # 找具体频道
    def find_channel_option(self, channel_name):
        return self.driver.find_element(self.channel_option[0], self.channel_option[1].format(channel_name))

    # 找第一条文章
    def find_channel_artical(self):
        return self.find_elt(self.first_artical)


# 操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()
        self.driver = DriverUtils.get_app_driver()

    # 找到对应频道并点击
    def check_channel(self, channel_name):
        # 获取滑动区域
        area = self.index_page.find_channel_area()
        x = area.location["x"]
        y = area.location["y"]

        w = area.size["width"]
        h = area.size["height"]

        start_x = x + w * 0.75
        start_y = y + h * 0.5

        end_x = x + w * 0.25
        end_y = start_y
        # 在区域内中去具体某个频道
        while True:
            # 在获取元素之前先获取一下当前页面的所有信息
            page_old = self.driver.page_source
            try:
                # 如找到目标频道则点击
                self.index_page.find_channel_option(channel_name).click()
                break
            except Exception as e:
                # 如没有找到目标频道则滑动
                self.driver.swipe(start_x, start_y, end_x, end_y)
                # 滑动到最后也没有找目标频道则抛出异常
                # 再获取当前页面所有信息和滑动之前的进行对比如相当等则表示已经滑动到最后了
                if page_old == self.driver.page_source:
                    raise NoSuchElementException

    # 点击第一篇文章
    def click_first_artical(self):
        self.index_page.find_channel_artical().click()


# 业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 根据频道来搜索文章
    def test_query_article_by_channel(self,channel_name):
        # 选择频道
        self.index_handle.check_channel(channel_name)
        # 点击第一篇文章
        self.index_handle.click_first_artical()
