from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=chrome_driver)



class web():
    def __init__(self):
        time.sleep(1)

    def browser_open(self,url):
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get(url)
        return self.driver

    def input_text(self,locator_type,value,text):
        self.driver.find_element(by=locator_type,value=value).send_keys(text)
        time.sleep(1)

    def click(self,locator_type,value):
        self.driver.find_element(by=locator_type,value=value).click()
        time.sleep(1)

    def assert_1(self,locator_type,value,text):
        nickname=self.driver.find_element(by=locator_type,value=value).text
        assert text in nickname
        time.sleep(1)

    def quit(self):
        self.driver.quit()


