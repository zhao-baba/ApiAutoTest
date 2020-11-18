from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
sleep(5)

# 定位美图秀秀
mtxx = driver.find_element_by_accessibility_id('美图秀秀')
# 长按元素
pressed = TouchAction(driver).long_press(mtxx).perform()
# 拖动并释放元素
pressed.move_to(x=110,y=80).release().perform()
sleep(2)
# 点击确认删除
driver.tap([(600,730)])

sleep(5)
