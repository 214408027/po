import time

#包含公共的操作 ：查找元素，点击元素，输入内容...
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 查找一个元素
    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])

    # 点击元素的方法
    def click_element(self, loc):
        # 强制等待1秒
        time.sleep(1)
        self.find_element(loc).click()


    # 向输入框里面输入内容
    def input_edit_content(self, loc, content):
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)


    # 查找一组元素
    def find_elements(self, loc):
        return self.driver.find_elements(loc[0], loc[1])


