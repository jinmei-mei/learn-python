#Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
#Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
# 函数语法：
'''
range(stop)
range(start, stop[, step])
'''
# 参数：start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
# range()函数 包含左边不包含右边
#如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(5):    #生成0-4
    print(i)
print("===========")
for i in range(5,9): #5-8 
    print(i)
print("===========")
#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0,10,3):
    print(i)
print("===========")
#步长是负数案例
for i in range(-10,-100,-30):
    print(i)  
print("===========")
# 结合range()和len()函数以遍历一个序列的索引，如下：
a = ['Google','Baidu','Runoob','Taobao','QQ']
for i in range(len(a)):
    print(i,a[i])  #i代表下标，a[i] 列表中i下标的元素打印出来
print("=============")
# 使用range()创建列表
print(list(range(5))) # 利用list函数返回列表
print(list(range(0))) #空数组 []
print("=============")
