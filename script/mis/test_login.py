import time

from page.mis.login_page import LoginProxy
from utils import DriverUtils, element_is_exist
import pytest

# 1.定义测试类
@pytest.mark.run(order=102)
class TestMisLogin:

    # 2.定义类级别初始化方法
    def setup_class(self):
        # 启动浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建对应po业务层的对象
        self.login_proxy = LoginProxy()

    # 3.定义测试方法
    def test_mis_login(self):
        # 定义测试数据
        username = "testid"
        password = "testpwd123"
        # 调用业务层执行测试步骤的方法
        self.login_proxy.test_mis_login(username, password)
        # 执行结果断言
        is_suc = element_is_exist(driver=self.driver, text="管理员")
        assert is_suc

    # 4.定义类级别销毁的方法
    def teardown_class(self):
        # 关闭浏览器
        time.sleep(2)
        DriverUtils.quit_mis_driver()
