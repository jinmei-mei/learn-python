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
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
'''
# 可更改(mutable)与不可更改(immutable)对象
# 在python中，strings，tuples和numbers 是不可更改的对象，而list，dict等则是可以修改的对象
# 1. 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
# 2.可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# python 函数的参数传递：
# 1.不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 2.可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# 备注：形参和实参的概念
# 形参 就是形式上的参数，可以理解为数学的X，没有实际的值，通过别人赋值后才有意义，相当于变量。
# 实参 就是实际意义上的参数，是一个实际存在的参数，可以是字符串或是数字等。

#通过id()函数查看内存地址变化：

def change(a):
    print(id(a))




