from selenium import webdriver
from appium import webdriver as app_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random,yaml,time,openpyxl,logging,sys,smtplib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class BoxDriver:

    def __init__(self,broswer_type='Chrome',app=None):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.baidu.wenku",
            "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
            "deviceName": "127.0.0.1:62001"
        }
        if broswer_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif broswer_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif broswer_type == 'Ie':
            self.driver = webdriver.Ie()
        elif broswer_type == 'App':
            self.driver = app_webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)

    def get(self,url):
        '''
        打开网页
        url: 网页的地址
        '''
        self.driver.get(url)

    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()

    def implicitly_wait(self,time=10):
        '''
        隐式等待
        time: 最大等待时间，单位是秒, 默认等待时间是10秒
        '''
        self.driver.implicitly_wait(time)

    def wait(self,second):
        '''
        休眠
        second: 休眠的时间，单位是秒
        '''
        time.sleep(second)

    def webdriver_wait(self,selector):
        '''
        显示等待元素
        selector: 自定义定位方式
        '''
        locator = self.selector_to_locator(selector)
        WebDriverWait(self.driver,10,0.05).until(EC.presence_of_element_located(locator))

    def selector_to_locator(self,selector):
        '''
        把自定义的selector定位方式转换为selenium标准定位方式
        'id, account' -> (By.ID, 'account')
        selector: 自定义定位方式
        '''
        # 定位方式
        by = selector.split(',')[0].strip()
        # 定位方式的值
        value = selector.split(',')[1].strip()
        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by =='class_name' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT, value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH, value)
        elif by == 'css_selector' or by == 'css':
            locator = (By.CSS_SELECTOR, value)

        return locator

    def locate_element(self,selector):
        '''
        定位单个元素
        selctor: 自定义定位方式
        '''
        locator = self.selector_to_locator(selector)
        element = self.driver.find_element(*locator)
        return element

    def locate_elements(self,selctor):
        '''
        定位多个元素
        selctor: 自定义定位方式
        '''
        locator = self.selector_to_locator(selctor)
        elements = self.driver.find_elements(*locator)
        return elements

    def click(self,selector):
        '''
        单击元素
        selctor: 自定义定位方式
        '''
        self.locate_element(selector).click()

    def input(self,selector,value):
        '''
        向文本框写入值
        selector: 自定义定位方式
        value: 要写入的值
        '''
        # 先清理一下
        element = self.locate_element(selector)
        element.clear()
        # 然后再写入
        element.send_keys(value)
        
    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

    def close(self):
        '''
        关闭当前窗口
        '''
        self.driver.close()

    def switch_to_frame(self,selector):
        '''
        进入frame
        '''
        iframe = self.locate_element(selector)
        self.driver.switch_to.frame(iframe)

    def select_by_index(self,selector,index):
        '''
        根据index选择元素
        selector: 自定义定位方式
        index: 选项的索引
        '''        
        dept_element = self.locate_element(selector)
        depts = Select(dept_element)
        # 选择部门
        depts.select_by_index(index)
    
    def select_by_value(self,selector,value):
        '''
        根据value选择元素
        selector: 自定义定位方式
        value: 选项的value值
        '''        
        dept_element = self.locate_element(selector)
        depts = Select(dept_element)
        # 选择部门
        depts.select_by_value(value)

    def select_by_visible_text(self,selector,visible_text):
        '''
        根据visible_text选择元素
        selector: 自定义定位方式
        visible_text: 选项的索引
        '''        
        dept_element = self.locate_element(selector)
        depts = Select(dept_element)
        # 选择部门
        depts.select_by_visible_text(visible_text)
    
class BasePage:

    def __init__(self,driver:BoxDriver):
        self.driver = driver
        self.driver.implicitly_wait()
        self.driver.maximize_window()
        self.driver.get('http://localhost/ranzhi/www/')

class GetYaml:

    def load(self,file):
        '''
        加载yaml文件
        file: 文件路径
        '''
        with open(file,'r',encoding='utf-8') as yaml_file:
            config = yaml.load(yaml_file.read(),Loader=yaml.BaseLoader)
        return config

class GetExcel:

    def load(self,workbook,worksheet):
        '''
        加载Excel文件
        workbook: 工作簿路径
        worksheet: 工作表名
        '''
        # 打开工作簿
        book = openpyxl.load_workbook(workbook)
        # 获取指定的工作表
        sheet = book[worksheet]

        data = [tuple(cell.value for cell in row) for row in sheet]
        return data[1:]

class GetLogger:

    def __init__(self,path):
        '''
        path: 日志文件的路径
        '''
        self.path = path
        # 创建日志
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        # 指定日志输出的内容与格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def console(self,level,message):
        '''
        level: 日志等级
        message: 日志信息
        '''
        # 将日志写入到文件中，选取追加写模式
        fh = logging.FileHandler(self.path,mode='a',encoding='utf-8')
        # 设置文件日志等级
        fh.setLevel(logging.DEBUG)
        # 设置日志的格式与内容
        fh.setFormatter(self.formatter)
        # 将内容添加到日志文件
        self.logger.addHandler(fh)

        # 将日志输出到控制台
        sh = logging.StreamHandler(sys.stdout)
        # 设置控制台日志等级
        sh.setLevel(logging.DEBUG)
        # 设置日志的格式与内容
        sh.setFormatter(self.formatter)
        # 将内容添加到控制台
        self.logger.addHandler(sh)

        # 判断日志等级，进行相应的输出
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        # 避免日志重复输出
        self.logger.removeHandler(sh)
        self.logger.removeFilter(fh)
        # 关闭日志文件
        fh.close()

    '''
    console('debug',message) -> debug(message)
    '''
    def debug(self,message):
        self.console('debug',message)
    def info(self,message):
        self.console('info',message)
    def warning(self,message):
        self.console('warning',message)
    def error(self,message):
        self.console('error',message)
    def critical(self,message):
        self.console('critical',message)

class Email:

    def send(self,subject,path):
        try:
            # 邮件服务器地址
            smtpserver = 'smtp.163.com'
            # 邮件服务器端口号
            port = 25
            
            # 发件人账号
            sender = 'yr10158094@163.com'
            # 邮箱密码
            pwd = 'ENKXDXFUDWVFAXRT'
            # 收件人
            receiver = 'moderator@163.com;zxx147298870@163.com;bxk3154143826@163.com;lethe_2020@163.com;fk2013302552@163.com'

            # 创建邮件对象
            mail = MIMEMultipart()
            # 初始化发件人
            mail['from'] = sender
            # 添加收件人
            mail['to'] = receiver
            # 添加主题
            mail['subject'] = subject

            # 读取报告内容
            with open(path,'rb') as file:
                mail_body = file.read()
            
            '''邮件正文'''
            # 创建html格式的消息对象
            body = MIMEText(mail_body,'html','utf-8')
            # 将报告内容添加到邮件正文当中
            mail.attach(body)

            '''邮件附件'''
            # 创建base64格式的对象
            att = MIMEText(mail_body,'base64','utf-8')
            # 指定附件的类型
            att['Content-Type'] = 'application/octet-stream'
            # 指定浏览器的处理方式
            # D:\workspace\selenium\ranzhi\report\report_2020-10-20_15-01-26.html
            att['Content-Disposition'] = 'attachment;filename=%s'%path.split('\\')[-1]
            # 添加附件
            mail.attach(att)

            '''发送邮件'''
            # 创建SMTP对象
            smtp = smtplib.SMTP()
            # 连接服务器
            smtp.connect(smtpserver,port)
            # 登陆
            smtp.login(sender,pwd)
            # 发送
            smtp.sendmail(sender,receiver.split(';'),mail.as_string())
            # 关闭邮件服务
            smtp.close()
            print('邮件%s发送完毕!'%subject)
        except:
            raise NameError('邮件发送失败！')

        
if __name__ == "__main__":
    Email().send('报告',r'D:\workspace\selenium\ranzhi\report\report_2020-10-20_16-37-39.html')