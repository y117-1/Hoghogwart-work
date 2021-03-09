import allure
import pytest


@allure.feature("搜索模块")

class Test_Search():

    def Test_case1(self):
        print("case1")

    def Test_case2(self):
        print("case2")

    def Test_case3(self):
        print("case3")

@allure.feature("登陆模块")

class Test_Login():

    def Test_login_sucess(self):
        print("case1")
        pass

    def Test_login_sucess_a(self):
        print("case2")
        pass

    def Test_login_sucess_b(self):
        print("case3")
        pass

if __name__ == '__main__':
        pytest.main()
