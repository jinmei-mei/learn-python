# List 索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。
#更新列表 append()
list = ['Google','Runoob',1998,2019]
print('第三个元素：',list[2])
list[2]=2020
print('更新后的第三个元素：',list[2])
list1 = ['Google','Runoob','Taobao']
list1.append('Baidu')
print('更新后List元素：',list1)
#可以使用 del 语句来删除列表的的元素，如下实例：
list = ['Google', 'Runoob', 1997, 2000]
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)
print(len(list))  #列表元素个数
#列表还支持拼接操作：
a = ['a','b','c','d']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1]) # 第一个列表中的第二个对象
print(max(n))
# Python列表函数&方法
# len(list) 列表元素个数
# max(list)返回列表元素最大值 min(list) 最小的值 
#list(seq) 将元组转换为列表
# python list的方法11种 详情见https://www.runoob.com/python3/python3-list.html

