#登录失败
import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead


@pytest.fixture(params = DataRead.readyaml(r"zonghe\data_case\login_fail.yaml"))
def pass_data(request):#固定写法
    return request.param
def test_register_pass(url,baserquests,pass_data):
    print("===============================================")
    print(f"测试数据为：{pass_data['casedata']}")
    # print(f"预期结果为：{pass_data['expect']}")

    r = Member.getlogin(url, baserquests,pass_data['casedata'])
    print("===============================================")
    print(r.text)
    # 检查结果
    assert r.json()['code'] == str(pass_data['expect']['code'])