# List 索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。
# 列表都可以进行的操作包括索引，切片，加，乘，检查成员。
#更新列表； append()添加元素列表项
list8 = ['Google','Runoob',1998,2019]
print('第三个元素：',list8[2])
list8[2]=2020
print('更新后的第三个元素：',list8[2])
list1 = ['Google','Runoob','Taobao']
list1.append('Baidu')
print('更新后List元素：',list1)
print("===============")

#可以使用 del 语句来删除列表的的元素，如下实例：
list9 = ['Google', 'Runoob', 1997, 2000]
print ("原始列表 : ", list9)
del list9[2]
print ("删除第三个元素 : ", list9)
print(len(list9))  #列表元素个数
#列表还支持拼接操作,案例如下：
squares = [1,4,9,16,25]
squares += [36,49,64,81,100]
print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("===============")
#使用嵌套列表即在列表里创建其它列表，例如：
a = ['a','b','c','d']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1]) # 第一个列表中的第二个对象
print(max(n)) # 列表最大值3
print("===============")
# Python列表函数&方法
# len(list) 列表元素个数
# len(list) 参数：list -- 要计算元素个数的列表。返回值：返回列表元素个数。
list2 = ['Google','Baidu','Taobao']
print(len(list2))
list3 = list(range(5))   #创建一个0-4的列表
print(len(list3))
print("===============")

# max(list)返回列表元素最大值 min(list) 最小的值 
list4 = ['Google','Baidu','Taobao']
print(max(list4)) # 列表中元素为字符串的时候，max 函数的比较是根据 id 的大小来判断的。
print(min(list4))
print("===============")

#list(seq) 将元组或字符串转换为列表
# 元组和列表非常类似，元组的元素值不能修改，元组是放在括号中，列表是防御方括号中
#list( seq ) 参数：seq:要转换为列表的元组活字符串 ，返回值：返回列表
aTuple = (123,'Google','Runoob','Taobao')
list6 = list(aTuple) 
print('列表的元素是：',list6) #列表的元素是： [123, 'Google', 'Runoob', 'Taobao']
str = 'Hello,world'
list5  = list(str)
print("列表的元素：",list5) #列表的元素： ['H', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd']
print("===============")


