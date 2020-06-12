"""你是如何编写自动化测试用例?"""
# 我是使用pytest+selenium来编写的测试用例
# 首先:按命名规范以及文案形式具体测试用例去定义好一个测试类
# 其次:其实对于测试用例封装无非是将手工形式操作以代码脚本的形式进行重新，那我的思路是这样的：
# 在一个测试类中，我们可能会实现多个测试方法，例如一个功能模块的多个测试点或者一个测试点的多种测试数据
# 为了模式真实的手工测试情况，我们只需要打开一次浏览器和关闭一次浏览器，引入pytest单元测试框架中fixture
# 的一种思想，可以实现整个测试用例只会打开一次浏览器和关闭一次浏览器。
# 在fixutre使用是类级别的fixture,在里面的会通过调用封装好的一个工具类中获取浏览器驱动的方法来打开一个
# 测试网址。同时在fixture中会实例化好po文件中对应业务层的类的对象，方便测试方法调用具体的业务方法。
# 组织具体的测试方法，会先定义好对应测试数据，然后按照文案形式的测试用例去按顺序调用对应的业务层的方法，完成
# 完整测试操作步骤。完成之后会得到一个具体的结果或者是跳转到指定的页面，由于自动化测试是来帮助我们完成
# 回归测试的，所以对应结果的校验点做的比较简单，例如我们只需要判断执行完操作后页面是否存在某个元素即认为
# 成功，调用pytest内置的assert方法来断言实际的结果
# 最后就是关闭浏览器
# 这个就是我具体单个测试用例编写思路和方式。
from config import BASE_ARITCAL_TITLE
from page.mis.aduit_page import AduitProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, element_is_exist
import pytest

@pytest.mark.run(order=103)
class TestAduit:

    # 在fixture 打开测试网站
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        # 实例化首页的业务层对象
        self.home_proxy = HomeProxy()
        # 实例化审核文章业务层对象
        self.aduit_proxy = AduitProxy()

    # 定义测试方法，在测试方法中会调用已经封装好po文件中业务层中提供的业务方法来实现具体的测试操作
    def test_aduit_aritcal(self):
        # 定义测试数据
        title = BASE_ARITCAL_TITLE
        # 调用业务
        self.home_proxy.to_aduit_page()
        self.aduit_proxy.test_aduit_aritcal(title)
        # 断言
        assert element_is_exist(driver=self.driver, text=title)

    # fixture中关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
