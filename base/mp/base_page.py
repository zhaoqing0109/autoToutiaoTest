from utils import DriverUtils


# 对象库层-父类
class BasePage:

    def __init__(self):
        # 获取自媒体浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()

    # 公用元素定位的方法
    def find_elt(self, location):
        # 元素定位
        return self.driver.find_element(*location)


# 操作层-父类
class BaseHandle:
    # 公用模拟输入的方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
