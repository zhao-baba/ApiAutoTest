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

# 启动app
# 获取package名称和activity名称：adb shell dumpsys | find "mFocusedActivity"
# driver.start_activity('com.baidu.wenku','.splash.view.activity.WelcomeActivity')
# sleep(5)

# 关闭app
# driver.close_app()

# 安装app 参数为安装文件的路径
driver.install_app(r'd:\com.mt.mtxx.mtxx.apk')

sleep(10)
# 卸载  参数为包名
driver.remove_app('com.mt.mtxx.mtxx')

sleep(5)

