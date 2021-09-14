
# python list的方法11种 详情见https://www.runoob.com/python3/python3-list.html
#方法1 ：append() 方法用于在列表末尾添加新的对象。
# list.append(obj) 参数：obj：添加到列表末尾的对象，返回值：无返回值，但是会修改原来的列表
# append()实例：
list1 = ["Google","Runoob","Taobao"]
list1.append("Facebook")
print("更新后的列表：",list1)
print("===============")

#方法2：count() 方法用于统计某个元素在列表中出现的次数。
# list.count(obj) 参数obj：列表中统计的对象，返回值：返回元素在列表中出现的次数
alist = [123,'Google','Runoob','Taobao',123]
print("123元素的个数：" ,alist.count(123))
print("Runoob的元素个数：",alist.count('Runoob'))
print("===============")

#方法4：extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# list.extend(seq) 
# 参数 seq：元素列表，可以是列表、元组、集合、字典、若为字典，则仅会将键key作为元素一次添加至原列表的末尾。
#该方法没有返回值，但会在已存在的列表中添加新的列表内容。
list1= ['Google','Baidu','Taobao']
list2 = list(range(5)) # 创建一个0-4的列表
list1.extend(list2)
print("扩展后的列表：",list1)
print("===============")

# 不同数据类型：
# 语言列表
language = ['French','English','German']
#元组
language_tuple = ('Spanish','Porttuguese')
#集合
language_set = {'Chinese','Japanse'}
#添加元组元素到列表末尾
language.extend(language_tuple)
print("新的列表：",language)
# 添加集合元素到列表末尾
language.extend(language_set)
print("新的列表：",language)
print("===============")

#方法5:index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
#list.index(x[,start[, end]])
# 参数：x--查找的对象、start--可选，查找的起始位置，end---可选，查找的结束位置
#返回值：该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
#案例：
list1 = ['Google','Baidu','Taobao','Runoob']
print('Runoob 索引值为：',list1.index('Runoob'))
print('Taobao 索引值为：',list1.index('Taobao'))
# 加参数的案例：
list1 = ['Google','Baidu','Taobao','Facebook','QQ','Runoob']
# 从指定位置开始搜索
print('Runoob索引值为：',list1.index('Runoob',1))
print("===============")

# 方法6：insert() 函数用于将指定对象插入列表的指定位置。
#list.insert(index,obj)
#参数：index --对象obj粗腰插入的索引位置，obj--要插入列表中的对象
#返回值：没有返回值，但会在列表指定位置插入对象
# 案例以下实例展示了 insert()函数的使用方法：
list1 = ['Google','Runoob','Taobao']
list1.insert(1,'Baidu')
print('列表插入元素后为：',list1)
print("===============")

#方法7：pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# list.pop(index = -1)
# 参数：index--可选参数，要移除列表元素的索引值，不能超过列表的总长度，默认为index=-1.删除最后一个列表值
# 返回值：返回从列表中移除的元素对象
#案例：
list1 = ['Google','Runoob','Taobao']
list1.pop()
print('列表现在为：',list1)
list1.pop(0)
print('列表现在为：',list1)
print("===============")
#方法8：remove() 函数用于移除列表中某个值的第一个匹配项。
#list.remove(obj)
# 参数：obj-列表中要移除的对象
#返回值：没有返回值，但是会移除列表中的某一个值的第一个匹配项
list1 = ['Google','Runoob','Taobao','Baidu']
list1.remove("Taobao")
print("列表现在为：", list1)
list1.remove("Baidu")
print("列表现在为：", list1)
print("===============")
#方法8：reverse()函数用户反向列表中的元素
#list.reverse() 
#参数：NA
#返回值：该法没有返回值，但是会对列表的元素进行反向排序。
#案例：
list1 = ['Google','Runoob','Taobao','Baidu']
list1.reverse()
print("列表翻转后：", list1)
# 方法9：sort()函数用于对原列表进行排序，如果指定参数，则使用表函数指定的比较函数
#list.sort(key=None,reverse=False)
#参数：key --主要用来进行比较的元素，只有一个参数，具体的函数的参数就是取决于可迭代对象中，指定可迭代对象中的一个元素进行排序，
# reverse--排序规则，reverse =True 降序， reverse = False 升序（默认）。
# 返回值：该方法没有返回值，但是会对列表的对象进行排序。
#案例：
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print('List:',aList)
#以下实例降序输出列表：
#列表
vowels = ['e', 'a', 'u', 'o', 'i']
#降序
vowels.sort(reverse=True)
#输出结果
print("降序输出：",vowels)
print("===============")

#以下实例演示了通过指定列表中的元素排序来输出列表：
#获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
#列表
random = [(2,2),(3,4),(4,1),(1,3)] #（3，4）中的4 -》代表第二个元素，
# 指定第二个元素排序
random.sort(key=takeSecond)  #按照第二个元素的大小排序 --》（3，4）中的4 -》代表第二个元素，
print(takeSecond(random)) # 打印一下指定的random中的元素
#输出类别
print('排序列表：',random)
print("===============")

# 方法10：clear() 函数用于清空列表，类似于 del a[:]。
# list.clear() 参数：无，返回值：该方法没有返回值
list1 = ['Google', 'Runoob', 'Taobao', 'Facebook']
list1.clear()
print("列表清空后：",list1) # 空列表
print("===============")

#方法11：copy() 函数用于复制列表，类似于 a[:]。
#list.copy() 参数：无。返回值：返回复制后的新列表
#以下实例展示了 copy()函数的使用方法：
list1 = ['Google', 'Runoob', 'Taobao', 'Facebook']
list2 = list1.copy()
print("list2的列表：",list2)