#Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
# if语句
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3    
# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
#Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
# 1.每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
a = 1
while a<7:
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
    a = a+1
#if实例：
#Python规定：0、空字符串、None为False，其他数值和非空字符串为True。
var1 = 100
if var1:
    print("1-if表达式条件为true")
var2 = 0
if var2:
    print("2- if 表达式为true")
print("GoodBye")
# 狗的年龄计算判断
age = int(input("请输入狗的年龄："))
print(" ")
if age<=0:
    print("你是来搞笑的嘛？")
elif age==1:
    print("相当于14岁的人")
elif age==2:
    print("相当于22岁的人")
elif age>2:
    human = 22+ (age-2)*5
    print("对应人的年龄是：", human)

input("点击enter 键退出")
# 该实例演示了数字猜谜游戏
number = 7
guess= -1
print("数字猜字谜游戏")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
# 嵌套语句
num = int(input("请输入数字："))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以被2整除，但是不能被3整除")
else:
    if num%3==0:
        print("你输入的数字可以被3整除，但是不能被2整除")
    else:
        print("你输入的数字不能被2和3整除")