#1.list.count(x)返回 x 在列表中出现的次数。
#2.list.insert(i, x)在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
#3.list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
#4.list.index(x)返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
#5.list.remove(x)删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
#6.list.reverse()倒排列表中的元素。
#7.list.sort()对列表中的元素进行排序。
#8.list.pop([i])从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
# （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(1,-2)
print(a)
print(a.append(333))
print(a)
a.index(333)
print(a)
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出），用append()方法
# 可以把一个元素添加到堆栈顶，用不指定索引的pop()方法可以把一个元素从堆栈顶释放出来：
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# 将列表当作队列使用
#也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，
# 然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.appendleft("Huahua")
print(queue)
# 列表推导式
#1.列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
#2.每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
vec = [2,4,6]
print([3*x for x in vec])
print([[x,x**2] for x in vec]) #结果 [[2, 4], [4, 16], [6, 36]]
# 对序列里面的每一个元素逐个调用某方法
freshfruit = [' banana ',' loganberry  ','passion fruit  ']
print([weapon.strip() for weapon in freshfruit]) #strip 去除前后的空格，
# 使用if句子作为过滤器
vec = [2,4,6]
print([3*x for x in vec if x>3])   #[12, 18]
print([3*x for x in vec if x<2])   #[]
vec1 = [2,4,6]
vec2 = [4,3,-9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
# 等于如下：
for i in range(len(vec1)):
    print(vec1[i])
    print(vec2[i])
    print(vec1[i]*vec2[i])
# FIXME
print([str(round(355/113, i)) for i in range(1, 6)])
# 等于如下信息：
# 知识点：round( x [, n]  )，
# 参数：x -- 数字表达式。n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。
# 返回值：返回浮点数x的四舍五入值。
for i in range(1,6):
    a = str(round(355/113,i))
    print(a)
# 嵌套列表解析

# 嵌套列表解析
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print([row[i] for row in matrix for i in range(4)])
print("=========")
for i in range(4): # i为0，循环第一个元素，结束后，循环第二个元素
    for row in matrix: #循环matrix，第一排，第二排，第三排
        print(row[i])
transposed = []
for i in range(4):
    transposed_row= []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
# 这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
# 例如：
a = [-1,2,66.25,333,333,1234.5]
del a[1]    # 下标是1的元素2被删掉
print(a)
del a [2:4]
print(a)
del a[:] #删除所有的元素
print(a)
print("=========")
# 元组和序列
# 元组由若干逗号分隔的值组成，例如：
t = 12345,54321,'Hello'
print(t[1])
print(t)
print("=========")
# Tuples may be nested(嵌套):
u = t,(1,2,3,4,5)
print(u) #((12345, 54321, 'Hello'), (1, 2, 3, 4, 5))
print("=========")
# 如山所示：元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
# 集合
# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)# 删除重复的
print('orange' in basket) # 检测成员
print('crabgrass' in basket )
# 以下演示了两个集合的操作
a = set('abracadfera')
b = set('alacazam')
print(a)  #a 中唯一的字母
print(a - b) #在 a 中的字母，但不在 b 中
print(a | b  ) # # 在 a 或 b 中的字母
print(a & b)# 在 a 和 b 中都有的字母
print( a ^ b)# 在 a 或 b 中的字母，但不同时在 a 和 b 中
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# 字典
# 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
# 一对大括号创建一个空的字典：{}。
tel = {'jack': 4098, 'sape': 4139}
tel['guido']=3212 
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['huahua']=3243
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
print(dict([('spae',4123),('jack',4322),('guido',4098)])) #{'spae': 4123, 'jack': 4322, 'guido': 4098}
#字典推导可以用来创建任意键和值的表达式词典：
a = {x : x**2 for x in (2,4,6)}
print(a)
# 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {"galllahad":'the pure',"robin":'the brave',"huahua":'the pleasure'}
for k ,v in knights.items():
    print(k,v)
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i ,v in enumerate(['tic','kaixin','kuaile']):
    print(i,v)
# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('What is your {0}? It is {1}'.format(q,a))
# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1,10,2)):
    print(i)
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for b in sorted(set(basket)):
    print(b)

