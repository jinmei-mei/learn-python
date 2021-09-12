#字符串格式化
#  %s 格式化字符串,%d 格式化整数
print("我叫 %s 今年%d岁"%('小明',10))
#f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：
#用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。
name = 'Runoob'
print(f'hello {name}')
print(f'{1+2}')
w = {'name':'runoob','url':'www.baidu.com'}
print(f'{w["name"]} : {w["url"]}')
# Python 字符串内建函数 等大小写转换
# capitalize()
# 将字符串的第一个字符转换为大写

