# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
    print("程序自身在运行")
else:
    print("我来自另一模块")
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# 说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
#dir() 函数
#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# str.format() 的基本使用如下:
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
import math
print('常量PI的值近似为{0:.3f}'.format(math.pi))
table = {'Google':1,'Runoob':2,'Taobao':3}
for name ,number in table.items():
    print('{0:10}===>{1:10d}'.format(name,number))
#Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
str = input("请输入：")
print("你输入的内容是：",str)
# 读和写文件
# open() 将会返回一个 file 对象，基本语法格式如下:
# open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# 打开一个文件
f =  open('/tmp/foo.txt','w')
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()
# 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
f =  open('/tmp/foo.txt','r')
str = f.read()
print(str)
f.close()
# f.readline()
# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
f =  open('/tmp/foo.txt','r')
str = f.readline()
print(str)
f.close()
# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f =  open('/tmp/foo.txt','r')
str = f.readlines()
print(str)
f.close()
#另一种方式是迭代一个文件对象然后读取每行:
# 打开一个文件
f = open("/tmp/foo.txt", "r")
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()
# f.write()
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# 打开一个文件
f = open('/tmp/foo.txt','w')
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
f.close()
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
#FIXME
# f = open("/tmp/foo1.txt",'w')
# value = ("www.runoob.com",14)
# s = str(value)
# f.write(s)
# f.close()
