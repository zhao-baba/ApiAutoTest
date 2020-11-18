from appium import webdriver
from time import sleep

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.baidu.wenku",
  "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)

sleep(5)
driver.tap([(400,850)],2000)
sleep(10)
driver.tap([(350,940)],1000)
sleep(10)

# 从下向上滑动
driver.swipe(300,900,300,400,500)
sleep(5)
driver.close_app()
# sleep(2)
# 打开美图秀秀
# driver.tap([(220,700)])
# sleep(5)