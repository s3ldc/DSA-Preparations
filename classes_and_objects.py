class Test:
    x = 82
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Instance object method
    def show(self):
        print(self.a, self.b)

    @staticmethod
    def f2():
        print("Hello")

    @classmethod
    def f3(cls):
        print(cls.x)

t1 = Test(27, 92)
t2 = Test(72, 19)
t1.show()
t2.show()
Test.f3()
Test.f2()
t1.f2()
