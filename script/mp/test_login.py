import logging
import time
from parameterized import parameterized
from page.mp.login_page import LoginPorxy
from utils import DriverUtils, element_is_exist, build_data
import pytest


# 1.定义测试类
@pytest.mark.run(order=2)
class TestLogin:

    # 2.定义初始化方法
    def setup_class(self):
        # 获取自媒体端的浏览器驱动对象并且赋给driver的实例属性
        self.driver = DriverUtils.get_mp_driver()
        # 创建业务层对象
        self.login_proxy = LoginPorxy()

    # 3.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        # 关闭浏览器
        DriverUtils.quit_mp_driver()

    # 4.定义测试方法
    @parameterized.expand(build_data())
    def test_login(self, mobile, code):
        # 5.定义测试数据
        # mobile = "15811859004"
        # code = "246810"
        # 6.调用业务方法
        logging.info("{}用户开始执行登陆".format(mobile))
        self.login_proxy.test_login(mobile, code)
        # 7.执行断言结果
        logging.info("开始执行mp端登陆结果断言")
        is_suc = element_is_exist(driver=self.driver, text="江苏传智播客教育科技")
        assert is_suc
