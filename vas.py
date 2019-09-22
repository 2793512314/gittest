#!/usr/bin/python
#-*-coding:utf-8-*-

# print("这是abc里的代码")
# """
# if __name__ == '__main__':
# __name__     python会自动获取当前文件的名字
# __main__     代表当前文件的名字
# """
# # python的程序入口，只能在当前文件下执行相应的代码 ，
# # 离开这个文件则条件不成立了 就不会执行if下的代码
# if __name__ == '__main__':
#     print("这是if语句下的代码")


class A(object):

    def __init__(self):
        self.num1 = 100
        self.__num2 = 50

    def __pin(self):
        print(f"num1的数是：{self.num1}，num2的值是{self.__num2}")

class B(A):

    def demo(self):
        print(self.__num2)
        self.__pin()

b = B()
print(b.num1)
b._A__pin()
# b.demo()
print(b._A__num2)








