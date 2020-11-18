from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.baidu.wenku",
  "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
sleep(5)

# 按下 HOME键
driver.press_keycode(3)
# 按下音量键
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(25)
driver.press_keycode(25)
driver.press_keycode(25)
driver.press_keycode(25)
# driver.long_press_keycode()
# 长按电源键
driver.long_press_keycode(26)
sleep(5)