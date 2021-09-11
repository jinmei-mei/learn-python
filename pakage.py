                                                                                                
# import 与 from...import
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# import了sys，才能使用系统给你的sys.argv
# argv是sys模块的一个全局变量，也称sys模块的一个属性！ argv本身为一个list类型的对象，该对象持有的第1个元素是命令行中传入的模块名、从第2个元素开始（含），均为命令行中传入的参数
#「argv」是「argument variable」参数变量的简写形式，一般在命令行调用的时候由系统传递给程序。
#这个变量其实是一个List列表，argv[0] 一般是被调用的脚本文件名或全路径，和操作系统有关，argv[1]和以后就是传入的数据了。
import sys
print("++++++Python import mode+++++")
print('命令行参数为：')
for i in sys.argv:
    print(i)

print('\n python 路径为',sys.path)

# # 导入sys 模块的argv,path
# from sys import argv,path
# print("=======python from import========")
# print('python的path：',path)# 因为已经导入path成员，所以此处引用时不需要加sys.path
# webbrowser 里面的open()函数是一个可以启动一个新浏览器，打开指定的url
import webbrowser,sys
if len(sys.argv)>1:
    address = ''.join(sys.argv[1:])
webbrowser.open('https://map.baidu.com/@13523299,3641066,12z' + address)