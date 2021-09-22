
#方法1：str.capitalize()将字符串的第一个字符转换为大写
# 参数：无，返回值：返回一个首字母大写的字符串
#案例：
str = "this is string example from runoob ...woow!!!"
print("str.capitalize():",str.capitalize())  # this 的第一个字母大写This
print("==============")
#方法2：center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#str.center([width,fillchar])
# width --字符串的总宽度，填充字符
#返回值：返回一个指定的宽度width居中的字符串，如果width肖宇字符串宽度直接返回字符串，否则使用fillchar去填充
str = "[runoob]"
print("str.center(40，'*')",str.center(40,'*'))
print("==============")
# 方法3：count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# str.count(sub,start=0,end=len(string))
# 参数：sub--搜索的子字符串，
#      start --字符串开始搜索的位置，默认为第一个字符，第一个字符索引值为0
#      end --字符串中结束搜索的位置，字符中第一个字符的索引为0，默认为字符串的最后一个位置
#返回值：该方法返回字符串在字符串中出现的次数
# 案例：
str1 = 'www.runoob.com'
sub = 'o'
print("str1.count('o'):",str1.count(sub))
print("============")
str2 = 'www.runoob.com,www.runoob.com'
sub = 'run'
print("str2.count('sub'):",str2.count(sub,0,30))
print("============")
# 方法3：decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
#bytes.decode(encoding="utf-8", errors="strict")
# 参数：encoding -- 要使用的编码，如"UTF-8"。
# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
# 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
# 返回值：该方法返回解码后的字符串。
#案例：
str3 = '我是个菜鸟'
# encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
# 参数：encoding -- 要使用的编码，如: UTF-8。
# 参数：errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 
# 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
# 返回值：该方法返回编码后的字符串，它是一个 bytes 对象。
str_UTF8 = str3.encode("UTF-8")   #encode 是编码
str_GBK = str3.encode("GBK")
print(str3)
print("UTF-8 的编码：",str_UTF8)
print("GBK的编码：",str_GBK)
print("======下面是解码======")
print("UTF-8的解码：",str_UTF8.decode(encoding='UTF-8',errors='strict'))
print("GBK的解码：",str_GBK.decode(encoding='GBK',errors='strict'))
# 方法5：endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
# str.endswith(suffix[, start[, end]])
#参数：suffix -- 该参数可以是一个字符串或者是一个元素。start -- 字符串中的开始位置。end -- 字符中结束位置。
#返回值： 如果字符串含有指定的后缀返回 True，否则返回 False。
#案例：
Str = 'Runoob example ....wow!!!!'
suffix = '!!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix,20))
suffix = 'run'
print(Str.endswith(suffix))     # 不是以run结尾，所以返回是False
print(Str.endswith(suffix,0,19))
print("============")
'''
FIXME
#方法6：expandtabs() 方法把字符串中的 tab 符号 \t 转为空格，
# tab 符号 \t 默认的空格数是 8，在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。
# str.expandtabs(tabsize=8)
# 参数：tabsize -- 指定转换字符串中的 tab 符号 \t 转为空格的字符数。
# 返回值：该方法返回字符串中的 tab 符号 \t 转为空格后生成的新字符串。
# 案例：
str = "runoob\t12345\tabc"
print('原始字符串:',str)
print(len(str))
#默认8个空格
#runoob有6个字符，后面的\t填充2个字符
#12345有5个字符，后面的\t填充3个字符
print("替换\\t符号：",str.expandtabs())
print(len(str))
# 2个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号:', str.expandtabs(2))
# 3 个空格
print('使用 3 个空格:', str.expandtabs(3))
# 4 个空格
print('使用 4 个空格:', str.expandtabs(4))
# 5 个空格
print('使用 5 个空格:', str.expandtabs(5))
# 6 个空格
print('使用 6 个空格:', str.expandtabs(6))
'''
# 方法7：find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
# str.find(str,beg=0,end=len(string))
# 参数：str --指定检索的字符串，beg--开始索引默认为0，end--结束索引，默认为字符串的长度
# 返回值：如果包含子字符串返回开始的索引值，否则返回-1。
#案例：
str1 = "Runoob example....wow!!!"
str2 = 'exam'
print(str1.find(str2))
print(str1.find(str2,5))
print(str1.find(str2,10))  # 从下标10开始，查找在字符串里第一个出现的子串：查找不到返回-1
print('=========')
# 方法7：index() 方法检测字符串中是否包含子字符串 str ，
# 如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
#str.index(str, beg=0, end=len(string))
# str --指定检索的字符串，beg--开始索引，默认为0，end--结束索引，默认为字符串的长度
#返回值：如果包含字符串返回开始的索引值，否则抛出异常
#案例：
str1 = "Runoob example ...wow !!!!"
str2 ="exam"
print(str1.index(str2))
print(str1.index(str2,5))
# print(str1.index(str2,10))  #抛出异常
print('============')

# 方法8：isalnum() 方法检测字符串是否由字母和数字组成。
#str.isalunm()
# 参数：无，返回值:如果string至少有一个字符并且都是字母或数字则返回True。否则返回False
str1 = "Runoob2016" # 无空格
print(str1.isalnum()) #返回True
str2 = "www.runoob.com"
print(str2.isalnum())# 返回Fasle ，有点点，不是字符串
print('============')
# 方法9：Python isalpha() 方法检测字符串是否只由字母或文字组成。
# str.isalpha() 
# 参数：无，返回值：如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。
str1 = "runoob" 
print(str1.isalpha())
#字母和中文文字
str2 = "runoob菜鸟教程"
print(str2.isalpha())
str3 = "Runoob example...wow!!!" # 返回Fasle ，有点点，不是字符串
print(str3.isalpha())
print('============')
# 方法10：Python isdigit() 方法检测字符串是否只由数字组成。
# str.isdigit()
# 参数：无。返回值：如果字符串只包含数字则返回 True 否则返回 False。
str1 = "123456"
print(str1.isdigit())
str2 = "Runoob example...wow!!!"
print(str2.isdigit())  # 返回False
print('============')
#方法11：islower()方法检测字符串是否由小写字母组成。
# str.islower() 
# 参数：无，
# 返回值：如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
str1 = "RUNOOB example...wow!!!"
print(str1.islower())  #既有大写又有小写，返回False
str2 = "runoob example...wow!!!"
print(str2.islower()) #只有小写，返回True
print('============')
# 方法12：isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），
# 罗马数字，汉字数字。指数类似 ² 与分数类似 ½ 也属于数字。
# 参数:无，返回值：如果字符串中只包含数字字符，则返回True，否则返回False
str1 = "runoob2021"
print(str1.isnumeric())
str2 = "2423432432434.9" # 浮点型不是整数，返回False
print(str2.isnumeric())
str3 = "23432434"
print(str3.isnumeric())
str4 = "四" # 汉字数字
print(str4.isnumeric())
print('============')
#方法13：Python isspace() 方法检测字符串是否只由空白字符组成。
#str.sispace()
#参数：无。返回值：如果字符串只包含空格，则返回True，否则返回False
str1 = "     "
print(str1.isspace())
str2 = "Runoob example...wow!!!"
print(str2.isspace())
print('============')
# 方法14：istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
# 参数：无。返回值：如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
str1 = "This Is String Example...Wow!!"
print(str1.istitle())
str2 = "This is String example ...wow!!"
print(str2.istitle())
print('============')
# 方法15：isupper() 方法检测字符串中所有的字母是否都为大写。
#str.isupper() 参数：无。返回值：如果字符串中包含至少一个区分小写的字符，并且所有这些（区分大小写的）字符都是大写，则返回True。否则返回False
str1 = "THIS IS STRING EXAMPLE....WOW!!!"
print(str1.isupper())
str2 = "THIS is string example....wow!!!"
print(str2.isupper())
print('============')
# 方法16：Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#参数：sequence -- 要连接的元素序列。返回值：返回通过指定字符连接序列中元素后生成的新字符串。
# str.join(sequence) 函数中的 sequence 中的元素必须的字符串，否则会报错
s1 = "-"
s2 = " "
seq = ("r","u","n","o","o","b")
print(s1.join(seq))
print(s2.join(seq))
print('============')
#当连接对象为 Dict 字典时，将所有的键 key 按顺序连接，其他的
# s1 = " "
Dict = {"I":"I","Love":"love","You":"you"} 
print(" ".join(Dict))
print('============')
# 案例
str1 = "abcdefg"
print(len(str1))
len1 = len(str1)-1   # 最大下标的获取 len1在这表表示下标，不是长度
print(len1)
str_list = []
while(len1>=0):
    str_list.append(str1[len1])
    print(str_list)
    print(str1[len1])
    len1=len1-1
print(''.join(str_list))

# 方法17：Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# len(s)
#参数 s 是对象，返回值：返回对象长度，长度是按照1开始
str1 = "Runoob"
print(len(str1)) #字母是6个字符，len就是6
l = [1,2,3,4,5]
print(len(l))# l的个数是5.len就是5
# 方法18：