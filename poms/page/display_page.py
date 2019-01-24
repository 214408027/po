
from base.base_action import BaseAction
import page


class DisplayPage(BaseAction):


    # 初始化函数， 在类初始化的时候这个init函数会执行， driver是外面传递过来的
    def __init__(self, driver):
        BaseAction.__init__(self, driver)


    # 点击显示
    def click_textview_display(self):
        # self.find_element(self.display_text_show).click()
        self.click_element(page.display_text_show)

    # 点击搜索
    def click_btn_search(self):
        # self.find_element(self.display_text_search).click()
        self.click_element(page.display_text_search)


    # 输入内容
    def input_search_edit_content(self, content):
        # self.find_element(self.display_input_edit_contnet).click()
        self.input_edit_content(page.display_input_edit_contnet, content)

    # 点击返回
    def click_btn_back(self):
        self.click_element(page.display_btn_back)

