# str1 = "abcdefg"
# print(len(str1))
# len1 = len(str1)-1   # 最大下标的获取
# print(len1)
'''
执行顺序
1.外层循环，for循环，n=2.
2.内层循环（第二层循环）range(2,2) 中间。x是0，for循环不成立，直接走else语句print(2,'是质数')
3.继续新的一轮循环，外层循环开始，第二层循环开始n=3,x=2, if条件不成立，继续第二层for循环,if条件不成立，直接走else语句print(3,'是质数')
4.n=4，if条件成立，走break，继续新的一轮外层for 循环依次类推
'''
# for n in range(2,10):
#     for x in range(2,n):
#         if n%x == 0:
#             print(n,'等于',x,'*',n//x)
#             break
#     else:
#         #循环中没有找到该元素
#         print(n,'是质数')

# '''
# 执行顺序
# 1.for循环开始，if条件不成立，直接print("执行pass块")
# 
# '''
for letter in "Runoob":
    if letter == 'o':
        pass
        print("执行pass块")
    print('当前的字母：',letter)
print("Good Bye")