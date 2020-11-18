from appium import webdriver
from time import sleep

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.baidu.wenku",
  "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62001"
}

# 打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
# 隐式等待
driver.implicitly_wait(30)

# sleep(3)
# 点击 “同意并继续”
driver.find_element_by_id('com.baidu.wenku:id/tv_agree').click()
# sleep(10)
# 关闭 ‘升级’
driver.find_element_by_id('com.baidu.wenku:id/dialog_pic_close').click()
sleep(10)

# 点击选中搜索框
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text').click()
# sleep(1)
# 输入搜索内容
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').send_keys('测试面试宝典')
# 点击搜索按钮
driver.find_element_by_id('com.baidu.wenku:id/h5_search_operate_text').click()
sleep(5)
# 断言

# 关闭
driver.close_app()