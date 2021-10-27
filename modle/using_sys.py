# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
import sys
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')

# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
# from modname import *
# 通过 modname.itemname 这样的表示法来访问模块内的函数。
