class Site:
    def __init__(self,name,url):
        self.name = name
        self.__url = url # private

    def who(self):
        print("name:",self.name)
        print("url:",self.__url)
    
    def __foo(self): #私有方法
        print("这是私有方法")
    
    def foo(self): # 公共的方法
        print("这是公共方法")
        self.__foo() 

x = Site("菜鸟教程","www.baidu.com")
x.who()
x.foo()
x.__foo() #报错
