from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import page

class SmsPage(BaseAction):

    # 初始化函数， 在类初始化的时候这个init函数会执行， driver是外面传递过来的
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 1.实现点击新增短信按钮
    # self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
    # 2.定位到接收者
    # self.driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys("100101")


    def click_newadd(self):
        self.click_element(page.new_add)

    def click_sms_edit(self, content):
        self.input_edit_content(page.sms_edit, content)

    def click_sms_input(self):
        self.click_element(page.input_sms_content)

    def sms_input_content(self, content):
        self.input_edit_content(page.input_sms_content, content)

    def sms_send_btn(self):
        self.click_element(page.sms_send_btn)

    def sms_verify(self, content):
        return self.find_elements(page.sms_send_lists)

