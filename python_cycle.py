# Python 中的循环语句有 for 和 while。
#一：while 循环一般形式如下：
'''
while 判断条件(condition)：
执行语句(statements)……
'''
# 案例 1：以下实例使用了 while 来计算 1 到 100 的总和：
n=100
sum=0 #来接收总和
counter = 1  
while counter<=n:
    sum = sum + counter
    counter+=1

print("1到%d的和是: %d" % (n,sum)) # 使用%是表述字符串输出
print("=============")
# 案例2：
#我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：
'''
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
 
print ("Good bye!")
'''
# while 循环使用 else 语句
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
'''
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''
# expr 条件语句为true,则执行statement(s)语句块，如果为false,则执行 additional_statement(s)
# 循环输出数字，并判断大小：
count = 0
while count<5:
    print(count,"小于5")
    count = count+1
else:
    print(count,"大于或者等于5")
print("==========")
  
#类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

'''
flag = 1
while(flag): print("欢迎来访问菜鸟教程")
print("Good bye")
'''

