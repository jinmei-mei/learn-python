# 字典是另一种可变容器模型，且可存储任意类型对象。
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
dict = {'Name':'Runoob','Age':7,'Class':'First'}
print("dict[Name]:",dict['Name'])
print("dict[Age]:",dict['Age'])
print("=============")
# 修改字典 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例：
dict1 = {'Name':'Runoob','Age':7,'Class':'First'}
dict1['Age'] = 9
dict1['School'] = '菜鸟教程'
print("dict1['Age']:",dict1['Age'])     #外面是单引号，里面必须是双引号
print("dict1['School']:",dict1['School'])
print("=============")
#删除字典元素
del dict1['Name']
print(dict1)
# 清空字典 clear()
dict1.clear()
print(dict1)
print("=============")
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# dict2  = {['Name']:'Rouoob','Age':90}
# print(dict2)    # 报错
# 字典内置函数& 方法
# len(dict) 计算字典元素个数，即键的总数
# str(dict) 输出字典，可以打印的字符串表示。
# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
# 方法1：clear() 清空删除所有元素，copy() 返回一个字典的浅复制
# 方法2： fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值，value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。实例如下：
seq= ('Name','Age','School')
dict = dict.fromkeys(seq)  #不指定值ß
print("新的字典为：%s" % str(dict)) #  字符串输出
dict = dict.fromkeys(seq,10) #设置对应值都为10
print("新的字典为：%s" % str(dict)) #  字符串输出
print("=============")
'''额外知识点'''
# Python 直接赋值、浅拷贝和深度拷贝解析
# 直接赋值：其实就是对象的引用（别名） b = a: 赋值引用，a 和 b 都指向同一个对象。
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
# 实例一：字典浅浅copy : b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
a = {1:[1,2,3]}
b = a.copy()
print(a,b)
a[1].append(4)
print(a,b)
print("=============")

#实例2 深度拷贝需要引入 copy 模块：b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
import copy
c = copy.deepcopy(a)
print(a,c)
a[1].append(5)
print(a,c)
print("=============")
# 方法3：Python 字典 get() 函数返回指定键的值。返回指定键的值，如果键不在字典中返回默认值 None 或者指定的默认值。
dict = {'Name':'Runoob','Age':10}
print("Age 的值为 %s" % dict.get('Age'))
print("Sex 的值为 %s" % dict.get('Sex','Na'))
print("=============")

# 方法4：in key in dict :key -- 要在字典中查找的键。
dict = {'Name':'Runoob','Age':90}
#检查键Age是否存在
if 'Age' in dict:
    print("Age 存在")
else:
    print("Age 不存在")
# not in 用法
if 'Age' not in dict:
    print("Age 不存在")
else:
    print("Age 存在")
print("=============")
# 方法5：Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
# dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
# 视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
# 我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
dict = {'Name':'Runoob','Age':90}
print('Value : %s' % dict.items())
# 遍历实例：
dict = {'Name':'Runoob','Age':90}
for i,j in dict.items():
    print(i,":\t",j) # \t 横向
print("=============")
# 方法 6：keys()和values()同上
dishes = {'eggs':2,'sausage':1,'bacon':1,'spam':500}
keys = dishes.keys()
values = dishes.values()
# 迭代
n = 0
for val in values:
    n = n+val     # n+=val
print(n)
# key 和Values 以相同顺序(插入顺序)进行迭代
print(list(keys))
print(list(values))
# 视图对象是动态的，受字典变化的影响，以下删除了字典的key，视图对象转为列表后也跟着变化
del dishes['eggs']
del dishes['sausage']
print(list(keys))   #['bacon', 'spam']
print("=============")
# 方法7：setdefault()：和get()类似
# 如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
# 而 get() 函数只返回默认值，并不改变原字典。
dict = {'Name': 'Runoob', 'Age': 7}
print("Age 键的值为 ：%s" % dict.get("Age"))
print("Sex 键的值为 ：%s" % dict.get("Sex")) # sex没有 
print(dict) # 结果{'Name': 'Runoob', 'Age': 7}
print("=============")
print("Age 键的值为 ：%s" % dict.setdefault("Age",None)) # age 有值，不需要默认值
print("Sex 键的值为 ：%s" % dict.setdefault("Sex",None)) # sex没有，新增并赋给与的值
print(dict)
print("=============")

# 方法8：update()：dict.update(dict2)  ==》dict2 -- 添加到指定字典dict里的字典。
# 方法9：Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 参数：key: 要删除的键值；default: 如果没有 key，返回 default 值
# 返回被删除的值。
site = {"name":"菜鸟教程","url":"www.Runoob.com"}
pop_obj = site.pop('name')
print(pop_obj) # 菜鸟教程
print(site)  #{'url': 'www.Runoob.com'}
print("=============")

# 方法10：Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。如果字典已经为空，却调用了此方法，就报出KeyError异常。
# 参数：无。返回值：返回一个键值对(key,value)形式，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
site = {"name":"菜鸟教程","alexa":"10000","url":"www.Runoob.com"}
pop_obj = site.popitem()
print(pop_obj) #('url', 'www.Runoob.com')
print(site) # {'name': '菜鸟教程', 'alexa': '10000'}

