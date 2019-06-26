from math import sin

class Calculator(object):


    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b


class Scientific_Calc(Calculator):


    def sin_func(self,x):
        return sin(x)


def test():
    c = Scientific_Calc()
    print c.add(2,3)
    print c.sub(3,5)
    print c.mul(3,3)
    print c.div(4.0,3)
    print c.sin_func(45)

if __name__ == '__main__':
    test()
