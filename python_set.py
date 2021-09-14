# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
baseket = {"apple","orange","apple","banana","orange"}
print(baseket) # 输出自动去重
print("orange" in baseket)
print("crabgrass" in baseket)
print("===================")

#集合的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)  # 集合a中包含而集合b中不包含的元素
print(a | b)   # 集合a或b中包含的所有元素
print(a & b )  # 集合a和b中都包含了的元素
print(a ^ b) # 不同时包含于a和b的元素
print("===================")

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # 结果 {'r', 'd'}
print("===================")
# 集合的基本操作
#1.s.add( x )   ==> 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
thisset = set(("Google","Taobao","Baidu"))
thisset.add("Facebook")
print(thisset)

#1.还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：s.update(x) x可以有多个，用逗号分开
thisset = set(("Google","Baidu","Taobao"))
thisset.update({1,2})
print(thisset)  # {1, 3, 'Taobao', 'Google', 'Baidu'}
thisset.update({3,4},[5,6])
print(thisset) #{1, 2, 3, 4, 5, 6, 'Taobao', 'Google', 'Baidu'}
print("===================")

# 2.移除元素 s.remove(x)==>将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
thisset = set(("Gooogel","Baidu","Taobao"))
thisset.remove("Taobao")
print(thisset)
#2.此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。s.discard( x ) 格式如下所示：
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

thisset = set(("Google","Baidu","Taobao"))
thisset.discard("Facebook") #不存在不会出错
print(thisset)
print("===================")
#3.设置随机删除集合中的一个元素，s.pop() 语法格式如下：
thisset = set(("Google","Baidu","Taobao","FaceBook"))
x = thisset.pop()
print(x) # 打印随机删除的元素
print(thisset)
print("===================")

#3.len(s) 计算集合 s 元素个数。
#4.清空集合 s.clear()，案例如下
thisset = set(("Google","Baidu","Taobao"))
thisset.clear()
print(thisset) #打印结果：set()
print("===================")
#5.判断元素是否在集合中存在： x in s ==》判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
thisset = set(("Google","Baidu","Taobao"))
print("Runoob" in thisset)
print("Taobao" in thisset)
print("===================")

#6. add()为集合添加元素，clear(),copy()拷贝一个集合，set.copy()；
# 7.difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
# set.difference(set) 参数：set -- 必需，用于计算差集的集合，返回值：返回一个新的集合。
#返回一个集合，元素包含在集合 x ，但不在集合 y ：
x = {"apple","banana","cherry"}
y = {"google","apple","mac"}
z = x.difference(y)
print(z)   # 返回一个新的集合 {'banana', 'cherry'}
print(x) # 结果是 {'cherry', 'apple', 'banana'}
# difference_update() 方法用于移除两个集合中都存在的元素。
#difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合
# 而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
x = {"apple","banana","cherry"}
y = {"google","apple","mac"}
x.difference_update(y)
print(x)    #结果是{'cherry', 'banana'}
print("===================")

# 方法8：set.discard(value) 该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
# 参数：必须的是需要移除的元素，返回值：无
fruit = {"apple","banana","orange"}
fruit.discard("apple")
print(fruit) # {'banana', 'orange'}
print(fruit.discard("pear"))  # 没报错，返回None
print("===================")
# 方法9：intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
# set.intersection(set1, set2 ... etc)
#  参数：set1 -- 必需，要查找相同元素的集合，set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
# 返回值：返回一个新的集合
# 案例：返回一个新集合，该集合的元素既包含在集合 x 又包含在集合 y 中：
x = {"apple","banana","cherry"}
y = {"google","apple","mac"}
z = x.intersection(y)
print(z)   #结果 {'apple'}
# 计算多个集合的交集：
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result  = x.intersection(y,z)
print(result) #{'c'}
# intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
# set.intersection_update(set1, set2 ... etc)
# 参数：set1 -- 必需，要查找相同元素的集合 ；set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
# 返回值：无
# 案例：移除 x 集合中不存在于 y 集合中的元素：
x = {"apple","banana","cherry"}
y = {"google","apple","mac"}
x.intersection_update(y) # # y 集合不包含 banana 和 cherry，被移除 
print(x)    # {'apple'}
# 计算多个集合的并集：
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y,z)
print(x)
# 方法10 ：isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# set.isdisjoint(set)
# 参数：set -- 必需，要比较的集合
# 返回值：返回布尔值，如果不包含返回 True，否则返回 False。
# 案例：判断集合 y 中是否有包含 集合 x 的元素：
# 如果包含返回 False：
x = {"apple","banana","cherry"}
y = {"google","apple","mac"}
z = x.isdisjoint(y)
print(z) # False
# 不包含
x = {"apple","banana","cherry"}
y = {"google","facebook","mac"}
z = x.isdisjoint(y)
print(z)# True
print("===================")

# 方法11 ：issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
#set.issubset(set)
#参数：set -- 必需，要比查找的集合
# 返回值：返回布尔值，如果都包含返回 True，否则返回 False。
#实例：判断集合 x 的所有元素是否都包含在集合 y 中：
x = {"a","b","c"}
y = {"f","e","d","c","b","a"}
z = x.issubset(y)
print(z)  # 全部包含 返回True
# 如果没有全部包含返回 False：
x = {"a","b","c"}
y = {"f","e","d","c","b"}
z = x.issubset(y)
print(z) #如果没有全部包含返回 False
# 方法12 ：issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
# set.issuperset(set)
# 参数：set -- 必需，要比查找的集合
# 返回值：返回布尔值，如果都包含返回 True，否则返回 False。
# 案例：判断集合 y 的所有元素是否都包含在集合 x 中：
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# 如果没有全部包含返回 False：
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
print("===================")

# 方法13：pop()随机移除，参数无，返回移除的元素。
# set.remove(item) item -- 要移除的元素，返回值：无
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits) # {'cherry', 'apple'}
print("===================")

# 方法13：symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
# set.symmetric_difference(set)
# 参数：set集合
# 返回值：返回一个新的集合
# 案例：返回两个集合组成的新集合，但会移除两个集合的重复元素：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.symmetric_difference(y)
print(z) # {'runoob', 'cherry', 'banana', 'google'}
# 方法14：symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
#set.symmetric_difference_update(set)
#参数：set：要检测的集合
#返回值：无
# 案例：在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的元素插入到集合 x 中：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.symmetric_difference_update(y)
print(x) # {'google', 'cherry', 'banana', 'runoob'}
print("===================")

# 方法14：union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
# 参数：set1 -- 必需，合并的目标集合，set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
# 返回值：返回一个新集合。
#案例：合并两个集合，重复元素只会出现一次：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z =x.union(y)
print(z) # {'apple', 'banana', 'google', 'cherry', 'runoob'}
# 合并多个集合：
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y,z)
print(result) # {'a', 'b', 'd', 'f', 'e', 'c'}
print("===================")
# 方法15：update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
# set.update(set)
# 参数：set 必须，可以是元素或者集合
# 返回值：无
# 案例：合并两个集合，重复元素只会出现一次：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.update(y)
print(x) # {'cherry', 'apple', 'banana', 'google', 'runoob'}




