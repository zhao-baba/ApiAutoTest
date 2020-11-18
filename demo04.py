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
sleep(3)

# 根据属性的值定位
# driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"同意并继续")]').click()
# sleep(10)
# driver.find_element_by_xpath('//android.widget.ImageView[contains(@resource-id,"com.baidu.wenku:id/dialog_pic_close")]').click()
# sleep(5)

# UiAutomator定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("同意并继续")').click()
# sleep(10)
# new UiSelector().resourceId()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.wenku:id/dialog_pic_close")').click()
# sleep(10)

# 组合定位
# driver.find_element_by_android_uiautomator('className("android.widget.TextView").text("同意并继续")').click()
# sleep(10)
# driver.find_element_by_android_uiautomator('className("android.widget.ImageView").resourceId("com.baidu.wenku:id/dialog_pic_close")').click()
# sleep(10)


# 文本定位
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("同意并继")').click()
# sleep(5)

# 利用元素之间的关系定位
# 父子关系
# driver.find_element_by_android_uiautomator('className("android.widget.FrameLayout").childSelector(text("同意并继续"))').click()
# 兄弟关系
driver.find_element_by_android_uiautomator('text("不同意").fromParent(text("同意并继续"))').click()

driver.close_app()

# 打开美图秀秀 - content-desc属性
# driver.find_element_by_android_uiautomator('new UiSelector().description("美图秀秀")').click()
# sleep(5)
# driver.quit()
