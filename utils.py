# 导包
import json
import app
import logging
from logging import handlers

# 编写初始化日志的代码
# 1.首先定义一个初始化日志的函数
def init_logging():
    # 2.在函数中，设置日志器
    logger = logging.getLogger()
    # 3.设置日志等级
    logger.setLevel(logging.INFO)
    # 4.设置控制台处理器
    sh = logging.StreamHandler()
    # 5.设置文件处理器（文件处理的作用是设置保存日志的文件地址的）
    log_path = app.BASE_PATH + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when="M",
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 6.设置格式化器
    fmt ='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7.将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8.将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

# 封装通用断言函数
def assert_common(self,http_code,success,code,message,response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 编写读取登录数据的函数
def read_login_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData:  # type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    print("查看读取的登录数据为：", result_list)
    return result_list

# 编写读取员工模块数据的函数：
def read_emp_data(filepath,intetface_name):
    # 打开数据文件
    with open(filepath,mode="r",encoding="utf-8") as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        emp_data = jsonData.get(intetface_name) #type:dict
        # 遍历json格式的数据文件，并把数据处理成列表元组形式添加到空列表中
        result_list = list()
        result_list.append(tuple(emp_data.values()))

    print("读取到的{}员工数据为：{}".format(intetface_name,result_list))
    return result_list

# 只有在当前函数运行时，才会运行这里面的代码
if __name__ == '__main__':
    # 定义数据文件的目录（注意这个路径指向数据文件一定需要存在）
    filepath = app.BASE_PATH + "/data/login_data.json"
    # 读取路径中的数据，并接收返回结果
    result = read_login_data(filepath)
    # 打印返回的结果
    print("返回的result_list的结果为：",result)

    # 定义员工数据路径
    filepath2 = app.BASE_PATH + "/data/emp_data.json"
    # 读取员工数据
    read_emp_data(filepath2,"add_emp")
    read_emp_data(filepath2,"query_emp")
    read_emp_data(filepath2,"modify_emp")
    read_emp_data(filepath2,"delete_emp")

