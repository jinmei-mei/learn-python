# python 中变量不需要声明，变量使用前必须赋值，赋值后的变量才会被创建
# 变量没有类型，”类型“是变量所指的内存中对象的类型
# 用 = 来给变量赋值，运算符左边是一个变量名，一遍是存储在变量中的值
counter = 100 # 整型变量
miles = 10000.0 #浮点型变量
name = 'Python' #字符串
print(counter)
print(miles)
print(name)
print('=============')
# 多个变量赋值
a,b,c =1,2,'python'
print(a,b,c)  #两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c
print('=============')
# 标准数据类型
#不可变的三种：number、string、tuple（元组）
#可变的三种：List、Dictionary、Set(集合)
# Number(数字) Python3 支持 int、float、bool、complex（复数）。
#Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
#内置的 type() 函数可以用来查询变量所指的对象类型。
a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
print('=============')
#还可以用 isinstance 来判断
# isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。 
class A:
    pass
class B(A):
    pass

print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)
print('=============')
#Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
# issubclass 子类 ，isinstance  实例
print(issubclass(bool,int))
print(True == 1)
print(False == 0)
print(True+1)
print(False+1)
print(1 is True)
print(0 is False)
print('=============')
# 指定要给值时，Number 对象就会被创建,del 删除对象引用
# var1 = 1
# var2 = 2
# del var1
# del var1, var2
# 数值运算 + - * /(得到的是浮点型)，//(返回整数)，%(取余数)，**(乘方)
# Python可以同时为多个变量赋值，如a, b = 1, 2。
# 在混合计算时，Python会把整型转换成为浮点数

print('=============')

# String Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 索引是0开始值，-1是末尾开始位置
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# Python 没有单独的字符类型，一个字符就是长度为1的字符串
# Python中的字符串不能改变
str = 'Runoob'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串
print('=============')

# List 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 加号 + 是列表连接运算符，星号 * 是重复操作
# List 索引值以 0 为开始值，-1 为从末尾的开始位置。
list = ['abcd',123,2.43,'Python',77.2]
tinyList = [123,'Python']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinyList * 2)    # 输出两次列表
print (list + tinyList) # 连接列表
print('=============')
# 与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1,2,3,4,5,6]
a[0]=9
a[2:5]=[11,12,13,14]
print(a)
a[2:5] = [] # 将对应的元素值设置为 []
print(a)
# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters = ['r','u','n','o','o','b']
print(letters[1:4:2])
print('=============')

# 元组
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 =() #空元组
tup2 = (10,) # 一个元素，需要再元素后面添加逗号
#string、list 和 tuple 都属于 sequence（序列）

print('=============')

# Set（集合）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 重复的元素自动去掉
# Set 可以进行集合的运算
sites = {'Google','Facebook','Taobao','Baidu','Zhidu','Facebook'}
print(sites)
# 成员测试
if 'Taobao' in sites:
    print("Taobao 在site集合中")
else:
    print('Taobao 不在site集合中')

# 集合运算
a = set('abcddfefedfd')
b= set('agerererd')
print(a)
print(a-b) # a和b的差集
print(a | b) # a和b的并集
print(a & b) #a和b的交集
print(a^b)  #a和b中不同时存在的元素
print('=============')
# Dictionary 字典
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = '1-菜鸟教程'
dict['two'] = '2-菜鸟工具'
tinydict = {'name':'Runoob','code':'1','site':'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict['two'])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print('=============')
#构造函数 dict() 可以直接从键值对序列中构建字典如下：交互式命令中可以执行成功
# >>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Runoob': 1, 'Google': 2, 'Taobao': 3}
# >>> {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
# >>> dict(Runoob=1, Google=2, Taobao=3)
# {'Runoob': 1, 'Google': 2, 'Taobao': 3}
# >>>