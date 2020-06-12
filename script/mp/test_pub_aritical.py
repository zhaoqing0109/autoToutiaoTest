import time

from config import BASE_ARITCAL_TITLE
from page.mp.home_page import HomePorxy
from page.mp.publish_page import PubProxy
from utils import DriverUtils, element_is_exist
import pytest


# 1.定义测试类
@pytest.mark.run(order=3)
class TestPubAritical:
    # 2.定义类级别初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建所需要页面的业务层的对象
        self.home_proxy = HomePorxy()
        self.pub_proxy = PubProxy()

    # 3.定义类级别销毁的方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()

    # 4.定义测试方法
    def test_pub_aritical(self):
        # 5.组织测试数据
        title = BASE_ARITCAL_TITLE
        content = "1.面试官不太美丽，2.沟通不太顺畅"
        option = "数码产品"
        # 6.调用业务层的方法
        self.home_proxy.to_publish_page()
        self.pub_proxy.test_pub_aritcal(title, content, option)
        # 7.断言实际结果 "新增文章成功"
        is_suc = element_is_exist(driver=self.driver, text="新增文章成功")
        assert is_suc
