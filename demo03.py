from appium import webdriver
from time import sleep

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
#   "appPackage": "com.baidu.wenku",
#   "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
# sleep(3)
# driver.close_app()

# 打开美图秀秀
# accessibility_id指的是content-desc属性的值
driver.find_element_by_accessibility_id('夜神应用中心HD').click()
sleep(5)
driver.quit()