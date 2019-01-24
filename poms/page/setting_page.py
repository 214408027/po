
from base.base_action import BaseAction
import page


class SettingPage(BaseAction):


    # 初始化函数， 在类初始化的时候这个init函数会执行， driver是外面传递过来的
    def __init__(self, driver):
        BaseAction.__init__(self, driver)


    # 点击搜索
    def click_search_btn(self):
        self.click_element(page.search_btn)


    # 输入内容
    def input_search_edit_content(self, content):
        self.input_edit_content(page.search_input, content)

    # 点击返回
    def click_btn_back(self):
        self.click_element(page.search_back_btn)

