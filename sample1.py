#第一个代码
print("Hello,Python")
#python 的关键字
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#行与缩进
if True:
    print("True")
else:
    print("False")
# 多行语句:语句很长，我们可以使用反斜杠 \ 来实现多行语句
total = 'item_one' + \
        'item_two' + \
        'item_three'
print(total)
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
#转义符 \
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 这里的 r 指 raw，即 raw string，会自动将反斜杠转义
print('\n') # 输出空行
print(r'\n') #输出\n

# 等待用户输入
input("\n\n 按下 enter 键后退出")

