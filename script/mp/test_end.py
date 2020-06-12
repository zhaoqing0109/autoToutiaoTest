from utils import DriverUtils
import pytest


@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 打开关闭浏览器开关
        DriverUtils.change_mp_key(True)
        # 调用关闭浏览器的方法
        DriverUtils.quit_mp_driver()