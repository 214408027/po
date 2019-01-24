# 告诉pytest在检索目录的时候，把当前目录也进行检索
import os,sys
sys.path.append(os.getcwd())

import time
from base.init_driver import init_driver
from page.network_page import NetworkPage
import page

class TestSetting:
    def setup(self):
        self.driver = init_driver(page.app_settings, page.app_settings_activity)
        self.network_page = NetworkPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    # 修改2g网络
    def test_updata_2g(self):

        # 点击更多
        self.network_page.click_text_more()

        # 移动网络
        self.network_page.click_text_mobile_net()

        # 首选网络
        self.network_page.click_text_first_network()

        # 点击2G
        self.network_page.click_2G()


    # 修改3g网络
    def test_updata_3g(self):

        # 点击更多
        self.network_page.click_text_more()

        # 移动网络
        self.network_page.click_text_mobile_net()

        # 首选网络
        self.network_page.click_text_first_network()

        # 点击3G
        self.network_page.click_3G()


