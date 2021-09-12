# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间
#Python 支持三种不同的数值类型：int float,complex(复数)
# int(x) 将x转换为一个整数。

# float(x) 将x转换到一个浮点数。

# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。

# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
# Python 取整函数
#1.向下取整 就是小 int()函数
a = 3.75
print(int(a))
# 2、四舍五入 round()函数
print(round(3.45))
print(round(8.89))
#3、向上取整，就是大：向上取整需要用到 math 模块中的 ceil() 方法:

import math
print(math.ceil(3.25))  # 4.0
print(math.ceil(3.75)) # 4.0
print(math.ceil(4.85)) # 5.0
