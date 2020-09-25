import pytest





#
# @pytest.fixture(scope="session") # 作用域
# def aa():
#     print("fixture函数被运行了")
#     return 11
#
# class Test111():
#     def test_aa(self,aa):
#         print(aa)
#
#     def test_bb(self,aa):
#         print(aa)
#
# class Test222():
#     def test_aa(self,aa):
#         print(aa)
#     def test_bb(self,aa):
#         print(aa)
#
#
#
# import pytest
# @pytest.fixture(scope="class") # 作用域
# def aa():
#     print("fixture函数被运行了")
#     return 11
#
# @pytest.fixture() # 作用域
# def bb():
#     print("fixture函数被运行了")
#     return 11
#
# @pytest.mark.usefixtures("aa","bb")
# class Test111():
#     def test_aa(self):
#         print(111)
#     def test_bb(self):
#         print(111)
#
#
#
# import pytest
# @pytest.fixture(autouse=True) # 作用域
# def bb():
#     print("fixture函数被运行了")
#     return 11
#
#
# class Test111():
#     def test_aa(self):
#         print(111)
#     def test_bb(self):
#         print(111)



import pytest
@pytest.fixture(scope="class") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

@pytest.fixture(autouse=True) # 作用域
def bb():
    print("fixture函数被运行了")
    return 11





class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)

class Test222():
    def test_aa(self):
        print(11)
    def test_bb(self):
        print(111)



class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)

class Test222():
    def test_aa(self):
        print(11)
    def test_bb(self):
        print(111)
