
import page
from base.base_action import BaseAction


class NetworkPage(BaseAction):


    # 初始化函数， 在类初始化的时候这个init函数会执行， driver是外面传递过来的
    def __init__(self, driver):
        # self.driver = driver
        BaseAction.__init__(self, driver)

    # 点击更多
    def click_text_more(self):
        self.click_element(page.network_text_more)

    # 点击移动网络
    def click_text_mobile_net(self):
        self.click_element(page.network_text_mobile_net)

    # 点击首选网络
    def click_text_first_network(self):
        self.click_element(page.network_text_first_network)

    # 点击2G
    def click_2G(self):
        self.click_element(page.network_2G)

    # 点击3G
    def click_3G(self):
        self.click_element(page.network_3G)



