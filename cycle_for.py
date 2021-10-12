
# Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
# for循环的一般格式如下：
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
# 案例：
language = ['C','C++','Perl','Taobao']
for x in language:
    print(x)
print("==========")
# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site == 'Runoob':
        print("这里是菜鸟教程")
        break
    print("循环数据" + site)
else:
    print("没有循环数据！")
print("完成循环！")
print("==========")
# 小插曲 range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(5): # 头开尾闭合 所以结果是0，1，2，3，4
    print(i)
print("==========")
# range()指定区间
for i in range(5,9): #结果是5，6，7，8
    print(i)
print("==========")
# 也可以使用range以指定数字开始并指定不同的增量（可以是负数，有时，也叫步长）
for i in range(0,10,2):  # 0，2，4，6，8
    print(i)
print("==========")
# 负数
for i in range(-10,-100,-30):
   print(i) 
# break 和 continue 语句及循环中的 else 子句
# break语句可以跳出for和while的循环体，如果你从for或while循环终止，任何对应的循环else块将不执行
# continue语句用来告诉python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if(len(site))!=4:
        continue     #if成立，continue继续走for循环，下面的都不执行，直到不能满足if条件，直接执行最后一句Done
    print(f"Hello,{site}")
    if site == "Runoob":
        break
print("Done")
print("==========")
# while 中使用 break：
n = 5
while n>0:
    n=n-1
    if n==2:
        break
    print(n)
print("循环结束")
print("==========")
# while 中使用 continue：
m = 5
while m>0:
    m-=1  # m = m-1
    if m == 2:
        continue
    print(m)
print("循环结束")
print("==========")

# 更多案例如下
#  第一个：：
for letter in 'Runoob':
    if letter == 'b': #第一个字母R 不等于b，直接break跳出循环，执行print语句，第二次for循环开始
        break
    print("当前字母为:",letter)
    
print("==========")

# 第二个
'''
执行顺序：
while循环开始：
当var>0，执行print输出var
执行var=var-1
再走if判断条件，是否成立
不成立，继续while循环，直到if判断条件成立，执行break操作，跳出循环体，打印print("Good Bye")该程序执行完成
'''
var = 10
while var >0:
    print("当前的变量为为:",var)
    var=var-1
    if var == 5:
        break

print("Good Bye")
print("==========")
# 以下实例循环字符串 Runoob，碰到字母 o 跳过输出：
'''
执行顺序如下：
for循环开始
letter的第一个元素是R，if条件不成立，直接走print("当前字母：",letter)，
重新第二次（for循环），if条件不成立，直接走print("当前字母：",letter)，
当if条件成立时，走continue继续新的循环，for循环接下来if条件判断语句
直到for循环执行完成
'''
for letter in "Runoob":
    if letter =="o": # letter的第一个元素是R，if条件不成立，直接走print("当前字母：",letter)，重新第二次（for循环）;当if条件成立时，走continue继续新的循环for循环接下来if条件判断语句
        continue
    print("当前字母：",letter)
#循环语句可以有else子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
'''
执行顺序
1.外层循环，for循环，n=2.
2.内层循环（第二层循环）range(2,2) 中间。x是0，for循环不成立，直接走else语句print(2,'是质数')
3.继续新的一轮循环，外层循环开始，第二层循环开始n=3,x=2, if条件不成立，继续第二层for循环,if条件不成立，直接走else语句print(3,'是质数')
4.n=4，if条件成立，走break，继续新的一轮外层for 循环依次类推
'''
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,'等于','*',n//x)
            break
    else:
        #循环中没有找到该元素
        print(n,'是质数')
#Python pass是空语句，是为了保持程序结构的完整性。pass不做任何事情，一般就用作占位语句
# while True:
#     pass
# # 最小的类
# class MyEmptyClass:
#     pass
# 以下实例在字母为 o 时 执行 pass 语句块:
for letter in "Runoob":
    if letter == 'o':
        pass
        print("执行pass块")
    print('当前的字母：',letter)
print("Good Bye")
# 实例2
for char in 'PYTHON STRING':
    if char == ' ':
        break
    print(char,end="")
    if char == '0':
        continue

