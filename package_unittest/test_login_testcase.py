#存在的问题
"""
1.无法查看运行的用例数，比如成功了几条，失败了几条
2.如果失败了，是因为什么导致？最好给出失败的错误日志
3.无法去组织用例，不能控制哪些用例执行，哪些用例不执行？
"""

#解决方案：使用unittest去解决以上问题

#unittest的功能说明：
"""
a.TestCase()功能：
    1.可以进行断言
    2.测试可查看结果，可以查看失败的结果 
    3.可以进行初始化和清除功能

b.TestSuite()功能：
    1.可以添加不同问题的测试用例到套件中（单条）
    2.可以添加不同的测试用例组到套件中（一组）

c.TextTestRunner():
    1.可以将测试用例套件运行
d.TestLoader():
    1.可以进行批量运行测试用例 
"""
from projeck01.iter03add_user import login
import unittest
import sys
class TestLogin(unittest.TestCase):
#初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)
#清空类方法：
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)
#初始化方法
    def setUp(self) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)
#清除方法
    def tearDown(self) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)


#1.测试登录的测试用例
#case1：输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login("admin", "123456").get("code")
        self.assertEqual(except_value, actual_value)


#case2：输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("csd", "123456").get("code")
        self.assertEqual(except_value, actual_value)
#case3：输入空的用户名或密码登录
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("csd", "").get("code")
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    unittest.main()