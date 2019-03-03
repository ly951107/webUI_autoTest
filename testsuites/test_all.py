import unittest
import os
import HTMLTestRunner
# import sys
# sys.path.append("F:\lyUI\Discuz")
# from Discuz.testsuites.test1 import DiscuzTest1
# from Discuz.testsuites.test2 import DiscuzTest2
# from Discuz.testsuites.test3 import DiscuzTest3
# from Discuz.testsuites.test4 import DiscuzTest4


# 设置报告文件的保存路径
dir=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(dir,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
# 构造测试套件
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(DiscuzTest1))
# suite.addTest(unittest.makeSuite(DiscuzTest2))
# suite.addTest(unittest.makeSuite(DiscuzTest3))
# suite.addTest(unittest.makeSuite(DiscuzTest4))
# 加载测试用例
suite = unittest.TestLoader().discover("./", pattern="test*.py")
if __name__ == "__main__":
    html_report = report_path + r".\result.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)










