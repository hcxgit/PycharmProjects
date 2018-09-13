
import os
import json
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pymongo import MongoClient
from time import sleep
# from AppSpider.processor import Processor
# from AppSpider.config import *
import config
import sys
# print(sys.path)

class Moments():
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': NO_RESET
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        # 处理器
        self.processor = Processor()

    def login(self):
        """
        登录微信
        :return:
        """

        # 访问权限
        el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el1.click()
        el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el2.click()
        # 点击登陆按钮
        el3 = self.driver.find_element_by_id("com.tencent.mm:id/d1w")
        el3.click()
        # 点击使用微信号密码登陆
        el4 = self.driver.find_element_by_id("com.tencent.mm:id/bwm")
        el4.click()
        # 输入微信号并发送
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget."
            "LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget."
            "FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget."
            "LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")
        el5.send_keys(USERNAME)
        # 输入密码并发送
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget."
            "LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget."
            "FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget."
            "LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        el6.send_keys(PASSWORD)
        # 登陆
        # el7 = self.driver.find_element_by_id("com.tencent.mm:id/bwn")
        el7 = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/bwn')))
        el7.click()
        # 去掉提示
        el8 = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/alk")))
        el8.click()

    # el7 = self.driver.find_element_by_id("com.tencent.mm:id/ak_")
    # el7.click()
    # el8 = self.driver.find_element_by_id("com.tencent.mm:id/alk")
    # el8.click()
    def enter(self):
        """
        进入朋友圈
        :return:
        """
        # 发现
        el9 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/c9d"]')))
        el9.click()
        # 朋友圈
        el10 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/a9d"]')))
        el10.click()

    def crawl(self):
        """
        爬取
        :return:
        """
        a = 1
        relations = {}
        while a < 200:
            # 当前页面显示的所有状态
            items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                         '//*[@resource-id="com.tencent.mm:id/den"]//android.widget.FrameLayout')))
            # 滑动屏幕
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            # 遍历每条状态
            for item in items:
                # try:
                # 	# 昵称
                # 	nickname = item.find_element_by_id('com.tencent.mm:id/apv').get_attribute('text')
                # 	# 正文
                # 	content = item.find_element_by_id('com.tencent.mm:id/deq').get_attribute('text')
                # 	# 点赞
                # 	like = item.find_element_by_id('com.tencent.mm:id/dea').get_attribute('text')
                # 	print(nickname, content, like)
                # except NoSuchElementException:
                # 	pass

                try:
                    nickname = item.find_element_by_id('com.tencent.mm:id/apv').get_attribute('text')
                    # print(nickname)
                    # except NoSuchElementException:
                    # 	pass
                    # try:
                    # 	content = item.find_element_by_id('com.tencent.mm:id/deq').get_attribute('text')
                    # 	print(content)
                    # except NoSuchElementException:
                    # 	pass
                    # try:
                    like = item.find_element_by_id('com.tencent.mm:id/dea').get_attribute('text')
                    print(like)
                    print(nickname)
                    like = like.split(', ')
                    for k in like:
                        relations.setdefault(nickname, set()).add(k)
                except NoSuchElementException:
                    pass

                # 插入MongoDB
                # self.collection.update({'nickname': nickname, 'content': content, 'like': like}, True)

                # data = [{nickname: like}]
                # with open('data.json', 'w',encoding='utf-8') as file:
                # 	file.write(json.dumps(data,indent=2,ensure_ascii=False))

                # sleep(SCROLL_SLEEP_TIME)
            a += 1
        print(relations)
        # with open('circle_edges1.txt', 'w') as file:
        # 	file.write(repr(relations))   # 将整个字典以字符串的形式存取
        # with open('circle_edges1.txt', 'r') as file:
        # 	f = file.readline()
        print(f)

    def main(self):
        """
        入口
        :return:
        """
        # 登录
        self.login()
        # 进入朋友圈
        self.enter()
        # 爬取
        self.crawl()


if __name__ == '__main__':
    moments = Moments()
    moments.main()
