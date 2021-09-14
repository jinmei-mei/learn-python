# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
# 元组可以使用下标索引来访问元组中的值
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
print(type(tup3))
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
# tup3 = tup1 + tup2
# print(tup3)
# del tup1
# print("删除后的元组tuple",tup1)   #会报错
# 元组运算符 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。ß
# 元组内置函数 len(tuple),max(tuple),min(tuple),tuple(iterable)将可迭代系列转换为元组
list5= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list5)
print(tuple1)
print('==================')
# len(tuple)
tuple1 = ('Google','Baidu','Taobao')
print(len(tuple1))     
print('==================')
tuple2 = ('5','4','1')
print(max(tuple2))
print(min(tuple2))
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象
tup = ('r','u','n','o','o','b')
# id() 函数用于获取对象的内存地址。
print(id(tup)) # 查看内存地址 4344501928
tup = (1,2,3)
print(id(tup)) # 内存地址不一样了 4484479736




