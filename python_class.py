# 面向对象
'''
1.类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
2.方法：类中定义的函数。
3.类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
4.数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
5.方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
6.局部变量：定义在方法中的变量，只作用于当前实例的类。
7.实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
8.继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
9.实例化：创建一个类的实例，类的具体对象。
10.对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
11.Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
'''
#类定义
'''
语法格式如下：
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''
#类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。
#类对象支持两种操作：属性引用和实例化。
#属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
class MyClass():
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return "Hello,world"

# 实例化类
x =MyClass()
#访问类的属性和方法
print("MyClass 类的属性i为：",x.i)
print("MyClass 类的方法f输出为：",x.f)
print("==========")
# __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。例如:
class Complex:
    def __init__(self,realpart,iamgpart):
        self.r = realpart
        self.i = iamgpart

x = Complex(3.0,-4.5)
print(x.r,x.i)   # 输出结果：3.0 -4.5
print("========")
# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()
# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t = Test()
t.prt()

# 类的方法
# 解释：在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
# 类的定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性，私有属性在类外部无妨直接进行访问
#     __weight = 0
#     # 定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("{0}说：我{1}岁。".format(self.name,self.age))
#         # print("%s 说: 我 %d 岁。" %(self.name,self.age))


# # 实例化类
# p =people("runoob",4,50)
# p.speak()
# print("===========")
# 子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
# BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无妨直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("{0}说：我{1}岁。".format(self.name,self.age))
        # print("%s 说: 我 %d 岁。" %(self.name,self.age))
    
    # 单继承实例
class student(people):
    grade = ''
    def __init__(self, n, a, w,g):
        # 调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
        #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student("KEN",14,10,3)
s.speak()
# 多继承
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('我叫{0},我今年{1}岁',self.name,self.age)

# 单继承案例：
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
        # 覆盖父类的方法
        def speak(self):
            print('我叫{0},我今年{1}岁，上小学{2}年级'.format(self.name,self.age,self.grade))

# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫{0},我是一个演说家，我演讲的主题是{1}'.format(self.name,self.topic))

# 多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,t)
        speaker.__init__(self,n,t)

test = sample("Tim",20,4,80,'Python')
test.speak()# 方法名相同，默认调用的是在括号中排在前面的父类额方法

# 方法重写
# 定义父类
class Parent:
    def my_method(self):
        print("调用父类方法")

class Child(Parent):# 定义子类
    def my_method(self):
        print("调用子类方法")

c =Child() # 子类实例化
c.my_method() # 子类调用重写的方法
super(Child,c).my_method() # 用子类对象调用父类已被覆盖的方法

#类的是有属性和私有方法
# 1.私有属性：不能在类的外部被使用或直接访问
# 2.私有方法：只能在类的内部调用 ，不能在类的外部调用

# 类的私有属性实例如下：
class JustCounter:
    __secertCount = 0 #私有变量
    publicCount = 0 # 公开变量
    
    def count(self):
        self.__secertCount +=1
        self.publicCount +=1
        print(self.__secertCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secertCount)

# 类的私有方法实例：
class Site:
    def __init__(self,name,url):
        self.name = name
        self.__url = url # private

    def who(self):
        print("name:",self.name)
        print("url:",self.__url)
    
    def __foo(self): #私有方法
        print("这是私有方法")
    
    def foo(self): # 公共的方法
        print("这是公共方法")
        self.__foo() 

x = Site("菜鸟教程","www.baidu.com")
x.who()
x.foo()
x.__foo() #报错



        











        


        


