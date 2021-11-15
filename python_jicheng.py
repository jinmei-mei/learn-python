# super()函数
# super() 函数是用于调用父类(超类)的一个方法。
# super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
# 语法
# super(type[, object-or-type])
# 参数：type ---类，object-or-type -- 类，一般是 self

class A:
    def add(self,x):
        y = x+1
        print(y)
class B(A):
    def add(self,x):
        super().add(x)

b = B()
b.add(3)



# 以下展示了使用 super 函数的实例：
class FooParent(object):
    def __init__(self):
        self.parent = "I\'m the parent"
        print('Parent')

    def bar(self,message):
        print("{0}from Parent".format(message))

class FooChild(FooParent):
    def __init__(self):
        super(FooChild,self).__init__()
        print('Child')

    def bar(self,message):
        super(FooChild,self).bar(message)
        print('Child bar function')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar("HelloWorld")






