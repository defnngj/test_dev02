import sys
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests
#import xmlrunner
from os.path import dirname, abspath
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
BASE_PATH = BASE_DIR.replace("\\", "/")
sys.path.append(BASE_PATH)

print("运行测试文件：", BASE_PATH)

# 定义任务的目录
TASK_PATH = BASE_PATH + "/resource/tasks/"


@ddt
class InterfaceTest(unittest.TestCase):

    @unpack
    @file_data("test_data_list.json")
    def test_run_casess(self, url, method, header, parameter_type, parameter_body, assert_type, assert_text):

        if header == "{}":
            header_dict = {}
        else:
            hearder_str = header.replace("\'", "\"")
            header_dict = json.loads(hearder_str)

        if parameter_body == "{}":
            parameter_dict = {}
        else:
            parameter_str = parameter_body.replace("\'", "\"")
            parameter_dict = json.loads(parameter_str)

        if method == "get":
            if parameter_type == "from":
                r = requests.get(url, headers=header_dict,
                                 params=parameter_dict)
                #self.assertIn(assert_text, r.text)

        if method == "post":
            if parameter_type == "from":
                r = requests.post(url, headers=header_dict,
                                  data=parameter_dict)
                #self.assertIn(assert_text, r.text)
			
            elif parameter_type == "json":
                r = requests.post(url, headers=header_dict,
                                  json=parameter_dict)
                #self.assertIn(assert_text, r.text)


# 运行测试用例
# def run_cases():
#     with open(TASK_PATH + 'results.xml', 'wb') as output:
#         unittest.main(
#             testRunner=xmlrunner.XMLTestRunner(output=output),
#             failfast=False, buffer=False, catchbreak=False)


if __name__ == '__main__':
    unittest.main()
