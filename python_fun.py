'''
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号 : 起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
'''
# def 函数名（参数列表）：
      #函数体
#比较两个数，并返回较大的数:
def max(a,b):
    if a>b:
        return a
    else:
        return b

a = 5
b = 6

print(max(a,b))

# 计算面积函数
def area(width,height):
    return width * height

def print_welcome(name):
    print("Welcome",name)

print_welcome("Python")
w=4
h=5
print("width =",w,"height =",h,"area =",area(w,h))
# 函数调用
#1.定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
#2.这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
# 如下实例调用了 printme() 函数：

# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return str


#调用函数
printme("我要调用用户自定义函数")
printme("再次调用同一个函数")

'''
参数传递
#在 python 中，类型属于对象，变量是没有类型的：
a = [1,2,3]
a = "Python"
# 以上代码中，[1,2,3] 是 List 类型，"Python" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
'''
# 可更改(mutable)与不可更改(immutable)对象
# 在python中，strings，tuples和numbers 是不可更改的对象，而list，dict等则是可以修改的对象
# 1.不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a。
# 2.可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# python 函数的参数传递：
# 1.不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是a的值，没有影响a对象本身。如果在fun(a)内部修改a的值，则是新生成一个a的对象。
# 2.可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# 备注：形参和实参的概念
# 形参 就是形式上的参数，可以理解为数学的X，没有实际的值，通过别人赋值后才有意义，相当于变量。
# 实参 就是实际意义上的参数，是一个实际存在的参数，可以是字符串或是数字等。

# 1.传不可变对象实例
#通过id()函数查看内存地址变化：

def change(a):
    print(id(a)) # 指向的是同一个对象
    a = 10
    print(id(a)) #一个新的对象

a=1
print(id(a))
change(a)
# 可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。
#2. 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
change(mylist)
print("函数外取值：",mylist)
# 参数 以下是调到用函数是可使用的正是参数类型
#1.必要参数
# 可写函数说明
'''
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return

# 调用printme函数，不加参数会报错
printme() #TypeError: printme() missing 1 required positional argument: 'str'
'''
#2.关键字参数
# 关键字参数核函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
# 使用关键字参数允许函数调用时参数的魂徐和声明时的不一致，因为Python解释器能用后参数名匹配参数值
# 一下实例在函数printme()调用时使用参数名
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

#调用printme函数
printme(str="菜鸟教程")

#如下案例：演示了函数参数的使用不需要使用指定顺序
# 可写函数说明

def printinfo(name,age):
    # 打印任何传入的字符串
    print("名字：",name)
    print("年龄：",age)
    return

# 调用printinfo函数
printinfo(age=40,name="Python")
print("================")

#3.默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数，以下实例中如果没有传入age参数，则使用默认值
# 可写函数说明
def printinfo(name,age=35):
    "打印任何传入的字符串"
    print("名字：",name)
    print("年龄：",age)
    return

# 调用printinfo函数
printinfo(age=50,name="Runoob")
print("=================")
printinfo(name="Runoob") # 不传入age的值，使用默认的值
print("=================")

#4.不定长参数
#可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名，基本语法如下：
'''
def funtionname([formal_args,] *var_args_tuple):
    "函数_文档字符串"
    function_suite
    return[expression]
'''
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vartuple)

#调用printinfo函数
printinfo(70,60,50)  
print("=================")
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用printinfo函数
printinfo(10)
print(70,60,50)
print("=================")

# 还有一种就是参数带两个星号 **基本语法如下：
'''
def functionname([formal_args,]**var_args_dict):
    "函数_文档字符串"
    function_suite
    return [expression]
'''
# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
def printinfo(arg1,**vardict):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vardict)

# 调用printinfo函数
printinfo(1,a=2,b=3)   # 带星号的参数以字典对的形式输出
print("=================")
#声明函数时，参数中的*号可以单独出现，例如：
def f(a,b,*,c):
    return a+b+c

print(f(1,2,c=3))# 正常
# print(f(1,2,3)) #报错
#匿名函数
'''
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
#语法 lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1,arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为：",sum(10,10))
print("相加后的值为：",sum(20,10))
print("=================")
#return[表达式]语句用于退出函数，选择性地向调用方返回一个表达式，不带参数值的return语句返回None，如下演示return语句的用法：
def sum(arg1,arg2):
    # 返回2个参数的和
    total = arg1 + arg2
    print("函数内：", total)
    return total     # return total 后，print("函数外：",total) 会打印函数外：80 。不带参数的return ，返回函数外： None

#调用sum函数
total = sum(30,50)
print("函数外：",total)
# 强制位置参数
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
'''
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


正确使用：
f(10, 20, 30, d=40, e=50, f=60)

以下使用方法会发生错误:
f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
'''
#FIXME递归函数

def factortial(n):
    if n ==0:
        return 1
    return n * factortial(n-1)


d = factortial(4)
print(d)
