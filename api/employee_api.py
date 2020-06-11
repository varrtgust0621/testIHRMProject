# 导包
import requests

# 创建要封装的员工类
class EmployeeApi:

    def __init__(self):
        # 定义员工模块的URL
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    # 添加员工
    def add_emp(self,username,mobile,headers):
        # 根据外部传入的 username 和 mobile 拼接成要发送的请求体数据
        jsonData = {
                    "username":username,
                    "mobile":mobile,
                    "timeOfEntry":"2020-06-08",
                    "formOfEmployment":1,
                    "departmentName":"测试部",
                    "departmentId":"1063678149528784896",
                    "correctionTime":"2020-05-30T16:00:00.000Z"
                    }
        # 发送添加员工请求并返回结果
        return requests.post(url=self.emp_url,json=jsonData,headers=headers)

    # 查询员工
    def query_emp(self,emp_id,headers):
        # 拼接查询员工的URL
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工请求并返回结果
        return requests.get(url=query_url,headers=headers)

    # 修改员工
    def modify_emp(self,emp_id,jsonData,headers):
        # 拼接修改员工的URL
        modify_url = self.emp_url + "/" + emp_id
        # 发送修改员工请求并返回结果
        return requests.put(url=modify_url,json=jsonData,headers=headers)

    # 删除员工
    def delete_emp(self,emp_id,headers):
        # 拼接删除员工的URL
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工请求并返回结果
        return requests.delete(url=delete_url,headers=headers)