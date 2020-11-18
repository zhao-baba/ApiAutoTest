'''
测试登录功能
'''
import pytest

from zonghe.baw import DbOp, Member
from zonghe.caw import DataRead



@pytest.fixture(params=DataRead.readyaml(r"ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml(r"ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param

# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserquests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserquests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db, phone)



def test_login(register, login_data,url, baserquests):
    # 登录
    # 检查登录结果
    r = Member.getlogin(url, baserquests, login_data['casedata'])
    assert r.json()['msg'] == login_data['expect']['msg']