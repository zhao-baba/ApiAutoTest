'''
注册的测试脚本（pytest）
'''
import pytest
from pytest_html.extras import json

from zonghe.baw import Member, DbOp
from zonghe.caw import DataRead

#测试前置：获取测试数据，数据是列表，通过readyaml读取来的



# @pytest.fixture(params = DataRead.readyaml(r"zonghe/data_case/register_fail.yaml"))
# def fail_data(request):#固定写法
#     return request.param
#注册失败
#
# def test_register_fail(url,baserquests,fail_data):
#     print(f"测试数据为：{fail_data['casedata']}")
#     print(f"预期结果为：{fail_data['expect']}")
#     #发送请求
#     r=Member.register(url,baserquests,fail_data['casedata'])
#
#
#     print(r)
#     #检查结果
#     assert r.json()['msg']==str(fail_data['expect']['msg'])


#注册成功
@pytest.fixture(params = DataRead.readyaml(r"zonghe/data_case/register_fail.yaml"))
def pass_data(request):#固定写法
    return request.param
def test_register_pass(url,baserquests,pass_data,db):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    phone=pass_data['casedata']['mobilephone']


    DbOp.deleteUser(db, phone)

    r = Member.register(url, baserquests, pass_data['casedata'])
    print(r)
    # 检查结果
    assert r.json()['code'] == str(pass_data['expect']['code'])

    #2.检查实际有没有注册成功(1.查找数据库2.获取用户列表，3.注册的用户登录）
    print("=================================")
    r=Member.getLiest(url,baserquests)
    print(r.text)
    assert phone in r.text

    #清理环境，根据手机号删除用户
    DbOp.deleteUser(db,phone)


#重复注册
def test_register_repeat():
     pass