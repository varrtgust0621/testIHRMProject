# 生成测试报告 是要先执行测试用例的
# 我们可以把测试用例添加到测试套件中，然后执行测试套件生成测试报告

# 1.导包
import os
import time
import unittest
import HTMLTestRunner_PY3
from script.test_ihrm_employee_params import TestIHRMEmployeeParams
from script.test_ihrm_login_params import TestIHRMLoginParams

# os.path.dirname(os.path.abspath(__file__)) 可以定位到当前项目的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2.创建测试套件
suite = unittest.TestSuite()
# 3.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLoginParams))
suite.addTest(unittest.makeSuite(TestIHRMEmployeeParams))
# 4.定义测试报告的目录和报告名称
report_path = BASE_DIR + "/report/tpshop{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 5.使用 HTML TestRunner_PY3生成测试报告
with open(report_path, mode='wb') as f:
    # 实例化 HTML TestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="IHRM接口功能测试",
                                               description="登录模块和员工管理模块")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)
