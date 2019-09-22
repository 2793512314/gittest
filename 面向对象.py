# -*- coding: utf-8 -*- 

# @Time : 2019/7/22 上午9:03 

# @Author : 废柴 

# @Project: teach

# @FileName : 面向对象.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# python --- 面向对象

# 类是对客观事物的抽象，对象是类的实例

# 类的书写格式
"""
class 类名():
    # 类的代码
    # 代码包括，循环、判断、函数
"""


# 定义一个动物园的类
class Zoo(object):   # (继承于哪一个类)
    # 属性
    dongwu = "老虎"

    # 方法
    def biaoyan(self):
        print(f"有一个神奇的动物，{self.dongwu}在表演!")

"""
object  # 翻译成中文叫做对象
object：所有类的基类
self: 在方法里面第一个参数必须是self
self 指代的是对象的本身

对象可以使用类的属性、方法

"""
# 类使用
# 第一步，创建对象
# a = Zoo()  # a对象
# 第二步，使用对象操作类的属性、方法
# print(a.dongwu)
# a.biaoyan()

"""
类的组成：
1、属性:
    # 从公有、私有的角度？
        公有的属性
        私有的属性
    # 从类、对象的角度？
        类属性
        对象属性 == 实例属性
2、方法
"""

print("--------------梦想分割线--------------")


# 学生类
class Student(object):

    # 类的属性
    book = ['言情系列', '武侠系列', '都市系列', '玄幻系列']

    # 初始化方法
    def __init__(self, name, grade, sex):
        # 对象的属性
        self.name = name  # name 的值 张三
        self.grade = grade
        self.sex = sex

    # 打印名字的方法
    def print_name(self):
        print(f"有个学生的名字叫做{self.name}")

    # 打印学生的班级
    def print_grade(self):
        print(f"有学生叫{self.name}，在{self.grade}班级里，他python学的贼好")

    # 打印学生的性别
    def print_sex(self):
        if self.sex:
            print("哇！靓仔!!!")
        else:
            print("哇！靓女!!!")

    # 打印学生书包里的图书
    def print_book(self):
        for i in self.book:
            print(f"书包里的书有：{i}")

# 类可不可以使用对象的属性、类属性?
"""
1、类不能使用对象的属性
类名 ---> 代表类
2、类可以访问类的属性
"""
# 对象可不可以使用对象属性、类属性?
"""
1、对象可以访问对象属性
2、对象可以访问类属性
"""
# A = Student("张三", 12, True)
# print(A.book)


# # 使用类的代码
# A = Student("张三", 12, True)
# A.print_name()
# A.print_grade()
# A.print_sex()
# A.print_book()
# print("--------------梦想分割线--------------")
# B = Student('李四', 13, False)
# B.print_name()
# B.print_grade()
# B.print_sex()


# 老师类

class Teacher(object):
    # 类属性: 公有  私有
    # 公有属性
    ke = ['语文', '数学', '外语', '生物']
    # 私有属性，双英文的下划线开头
    __grade = '1903'

    # 初始化方法、【魔法方法】
    def __init__(self, a, b):
        # 对象属性
        # 公有的对象属性
        self.a = a
        # 私有的对象属性
        self.__b = b
        self.c = "hello"

    # 实例方法
    def kl(self):
        print(f"方法访问类的公有属性：{self.ke}")
        print(f"方法访问类的私有属性：{self.__grade}")

    # 实例方法
    def g(self):
        print(f"方法访问对象的公有属性：{self.a}")
        print(f"方法访问对象的私有属性：{self.__b}")

    # 私有方法
    def __w(self):
        print("这是一个私有方法")

    # 在类的外部通过对象.方法名来访问方法，在类的内部，self.方法名来访问方法
    # self ===> 对象，访问方法、属性通过对象来操作
    # 实例方法
    def h(cls):
        cls.__w()


    # @在python里被称为语法糖
    @classmethod  # 装饰器：将一个实例方法变成类方法。
    def hello(cls):
        print("这是一个类方法")

    @staticmethod  # 装饰器： 将一个实例方法变成静态方法
    def python():  # 像一个没有参数的函数
        print("这是一个静态方法")


"""
私有属性定义的目的？
属性一旦被定义，不希望被更改
"""

# print(Teacher.ke)
# # 更改类属性对象的值
# Teacher.ke = (1, 2, 3)
# print(Teacher.ke)

# 更改对象属性，只能通过对象来修改它
t3 = Teacher(1, 2)
# 更改之前的
print(t3.c)
t3.c = "python"
t3.h()

"""
@classmethod  # 装饰器：将一个实例方法变成类方法。
类方法：参数是 cls 
cls self 都指向对象本身
cls 作为参数的方法可以通过类名.方法名访问
"""


# 对象.类方法名---> 访问类方法
t3.hello()
Teacher.hello()


# 更改之后的
print(t3.c)

t4 = Teacher('122', 2)
print(t4.c)

print('-------------梦想分割线--------------')
# 静态方法可以通过类名.静态方法名、对象.静态方法名来访问
Teacher.python()
t3.python()


# 在类的外部，类、对象都不能访问类的私有属性
# print(Teacher.__grade)
# print(t1.__grade)
# 对象可以访问类的私有属性、类的公有属性【在类的内部】
# t1 = Teacher()
# t1.kl()

# t2 = Teacher('hello', 'python')
# 私有的对象属性不能通过对象在类的外部访问
# print(t2.__b)
# 对象可以访问对象的私有属性、对象的公有属性【在类的内部】
# t2.g()


# 方法：静态、类方法、实例方法【普通方法】、魔法方法、
# 私有方法：
# def __方法名(self, 参数):










"""
创建对象的过程称为实例化。
当一个对象被创建之后，
包含3方面的特性：对象的标识、属性和方法。
Python自动给每个对象添加特殊变量self，
该变量指向对象本身，让类中的函数能够明确地引用对象的数据和函数。
类是由属性和方法组成。类的属性是对数据的封装，而类的方法则表示对象具有的行为。

Python的类的属性一般分为私有属性和公有属性，像C++有定义属性的关键字（public、private、protect），而Python没有这类关键字，默认情况下所有的属性都是“公有的”，对公有属性的访问没有任何限制，且都会被子类继承，也能从子类中进行访问。
若不希望类中的属性在类外被直接访问，就要定义为私有属性。Python使用约定属性名称来划分属性类型。若属性的名字以两个下划线开始，表示私有属性；反之，没有使用双下划线开始的表示公有属性。类的方法也同样使用这样的约定。
另外，Python没有保护类型的修饰符。

关于Python私有属性的访问：
- 类的外部不能直接访问私有属性。- Python提供了直接访问私有属性的方式，可用于程序的测试和调试。- 私有属性访问的格式：   instance._classname__attribute
    说明：
    instance表示实例化对象；
    classname表示类名；
    attibute表示私有属性
- 注意：classname之前是单下划线，attibute之前是双下划线
类的方法也分为公有方法和私有方法。私有方法不能被模块外的类或方法调用，私有方法也不能被外部的类或函数调用。
C++中的静态方法使用关键字static声明，而Python使用函数staticmethod()或@staticmethod修饰器将普通的函数转换为静态方法。Python的静态方法并没有和类的实例进行名称绑定，要调用除了使用通常的方法，使用类名作为其前缀亦可。
构造函数用于初始化类的内部状态，为类的属性设置默认值。 C++的构造函数是与类同名的方法，而Python的构造函数名为__init__。 __init__方法除了用于定义实例变量外，还用于程序的初始化。 __init__方法是可选的，若不提供__init__方法，Python将会给出1个默认的__init__方法
析构函数用于释放对象占用的资源。
Python提供了析构函数__del__()。析构函数也是可选的。若程序中不提供析构函数，Python会提供默认的析构函数。
当对象不再被使用时，__del__方法运行，但是很难保证这个方法究竟什么时候运行，若想指明它的运行，就要显式地调用析构函数：del 对象名
由于Python中定义了__del__()的实例将无法被Python的循环垃圾收集器（gc）收集，所以建议只有需要时才定义__del__。
事实上，使用Python编写程序可以不考虑后台的内存管理，直接面对程序的逻辑。
Python使用垃圾回收机制来清理不再使用的对象。Python提供gc模块释放不再使用的对象，Python采用“引用计数”的算法来处理回收，即：当某个对象在其作用域内不再被其他对象引用时，Python就自动清除该对象。
Python的函数collect()可以一次性收集所有待处理的对象（gc.collect()）
继承是面向对象的重要特性之一，可实现代码的重用。
通过继承可以创建新类，给既有类的副本添加变量和方法。
原始的类称为父类或超类，新类称为子类或派生类。
继承可以重用已经存在的数据和行为，减少代码的重复编写。
Python在类名后使用一对括号表示继承关系，括号中即为父类。
继承机制说明子类具有父类的公有属性和方法，而且子类可以扩展自身的功能，添加新的属性和方法。因此，子类可以替代父类对象，这种特性称为多态性。

此外，从根本上说，所谓多态性是指当不同的对象收到相同的消息时，产生不同的动作。
"""











