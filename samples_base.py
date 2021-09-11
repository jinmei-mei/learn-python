# 字符串实战 详情见有道笔记
str = '123456789'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 同一行显示多条语句
# print(obj)实质就是调用sys.stdout.write(obj+'\n') 
# sys.stdout是python中标准输出流# 两者等价sys.stdout.write('hello'+'\n') 最近，在发布脚本上线时，想要把输出结果和错误记录保存成日志（log），方便查看
import sys; x = 'python';sys.stdout.write(x + '\n') # 等价于print（x）
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
print('------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()   #不加这一行的话，打印出来是a b %
 