
# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input):
    # 通过空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 翻转字符
    #假设列表 List= = [1,2,3,4]
    #List[0]=1,List[1]=2,而-1表示最后一个元素，List[-1]=4(与List[3]=4一样)
    #inputWords[-1:-1]有三个参数
    #第一个参数-1，表示最后一个元素
    #第二个参数为空，表示移动到列表的末尾
    #第三个参数为步长，-1.表示逆向
    inputwords = inputwords[-1::-1]
    #重新组合字符串
    output = ' '.join(inputwords)
    return output


if __name__ == '__main__':
    input = 'I Like Python'
    re = reverseWords(input)
    print(re)

