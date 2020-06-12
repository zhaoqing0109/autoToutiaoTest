from page.app.index_page import IndexProxy
from utils import DriverUtils, element_is_exist


# 1.定义测试类
class TestQyAritcal:
    # 2.定义类级别初始化fixture
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.index_proxy = IndexProxy()

    # 3.定义测试方法
    def test_qy_ar_by_channel(self):
        # 组织测试数据
        channel_name = "数码产品"
        # 调用业务方法
        self.index_proxy.test_query_article_by_channel(channel_name)
        # 执行断言
        is_suc = element_is_exist(self.driver, "text", "猜你喜欢")
        assert is_suc

    # 4.定义类级别销毁fixture
    def teardown_class(self):
        DriverUtils.quit_app_driver()
