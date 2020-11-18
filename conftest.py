'''
脚本层的功夫方法
'''
import pytest


from zonghe.caw import DataRead#导入模块
from zonghe.caw.BaseRequests import BaseRequests#从模块中导入类

#从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return  DataRead.readIni("zonghe\data_env\env.ini","url")
#e
@pytest.fixture(scope='session')
def db():
    return eval(DataRead.readIni(r"zonghe\data_env\env.ini","db"))

#创建BaseRequests的一个实例
@pytest.fixture(scope='session')
def baserquests():
    return  BaseRequests()
