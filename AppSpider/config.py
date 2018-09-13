#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取  Lenovo_TB_8703F  OPPO_R9s
DEVICE_NAME = 'OPPO_R9s'

# APP路径
APP = os.path.abspath('.') + '/weixin.apk'

# APP包名
APP_PACKAGE = 'com.tencent.mm'

# 入口类名
APP_ACTIVITY = '.ui.LauncherUI'
# 不用重置
# NO_RESET = 'true'
# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 100

# 微信手机号密码
USERNAME = 'hcx812591452'
PASSWORD = '1993422hcx+yylv'

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 400

# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'

# 滑动间隔
SCROLL_SLEEP_TIME = 1
