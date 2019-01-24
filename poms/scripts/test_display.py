# 告诉pytest在检索目录的时候，把当前目录也进行检索
import os,sys
sys.path.append(os.getcwd())

import time
from base.init_driver import init_driver
from page.display_page import DisplayPage
import page

class TestSetting:
    def setup(self):
        # 初始化driver
        self.driver = init_driver(page.app_settings, page.app_settings_activity)
        self.display_page = DisplayPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    def test_display_search(self):
        # 点击显示
        self.display_page.click_textview_display()

        # 点击搜索按钮
        self.display_page.click_btn_search()

        # 输入内容
        self.display_page.input_search_edit_content('heheda')

        # 点击返回
        self.display_page.click_btn_back()

