import os,sys
sys.path.append(os.getcwd())

import pytest
from base.init_driver import init_driver
import time
from page.sms_page import SmsPage
import page
from base.read_yaml import read_yaml_data


# 读取sms_send.yaml数据
def get_data():
    data = read_yaml_data('sms_send.yaml')
    return data.get('send_data')


class TestSms:
    #获取driver
    def setup_class(self):
        self.driver = init_driver(page.app_sms, page.app_sms_activity)
        self.sms_page = SmsPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()



    def test_sms(self):
        #1.实现点击新增短信按钮
        self.sms_page.click_newadd()
        #2.定位到接收者
        self.sms_page.click_sms_edit('888888')

    #实现发送短信
    @pytest.mark.parametrize("content", get_data())
    def test_send_sms(self,content):
        #1.找到输入框
        self.sms_page.click_sms_input()
        #1.1输入内容
        self.sms_page.sms_input_content(content)
        #2.点击发送按钮
        self.sms_page.sms_send_btn()

        #3.验证发送成功
        sms_send_lists = self.sms_page.sms_verify(str)
        assert content in [i.text for i in sms_send_lists]



