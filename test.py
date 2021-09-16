# list2 = ['Google','Baidu','Taobao']
# print(len(list2))
# list3 = list(range(5))#创建一个0-4的列表
# print(len(list3))
# aTuple = (123,'Google','Runoob','Taobao')
# list6 = list(aTuple) 
# print('列表的元素是：',list6)
# str = 'Hello,world'
# list5  = list(str)
# print("列表的元素：",list5)


# def takeSecond(elem):
#     return elem[1]
# #列表
# random = [(2,2),(3,4),(4,1),(1,3)] 
# # 指定第二个元素排序
# random.sort(key=takeSecond)  #按照第二个元素的大小排序
# print(takeSecond(random)) # 打印一下指定的random中的元素
# #输出类别
# print('排序列表：',random)
# str_1 = input("输入一个字符串：")
# len1 = len(str_1)-1
# print(len1)
# str_list = []
# while(len1>=0):
#     str_list.append(str_1(len1))
#     len1=len1-1
# print(''.join(str_list))
str1 = "abcdefg"
print(len(str1))
len1 = len(str1)-1
print(len1)
str_list = []
while(len1>=0):
    str_list.append(str1[len1])
    print(str_list)
    print(str1[len1])
    len1=len1-1
print(''.join(str_list))
print(len(str_list))