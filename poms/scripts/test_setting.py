# 告诉pytest在检索目录的时候，把当前目录也进行检索
import os,sys
sys.path.append(os.getcwd())


import pytest

import time
from base.init_driver import init_driver
from page.setting_page import SettingPage
import page
from base.read_yaml import read_yaml_data

# 读取sms_send.yaml数据
def get_data():
    data = read_yaml_data('setting_data.yaml')
    return data.get('search_data')


class TestSetting:
    def setup(self):
        # 初始化driver
        self.driver = init_driver(page.app_settings, page.app_settings_activity)
        self.setting_page = SettingPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("content", get_data())
    def test_setting_search(self, content):

        # 点击搜索按钮
        self.setting_page.click_search_btn()

        # 输入内容
        self.setting_page.input_search_edit_content(content)

        # 点击返回
        self.setting_page.click_btn_back()


