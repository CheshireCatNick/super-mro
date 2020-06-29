class A:
    def hi(self):
        print('A')

class B(A):
    def hi(self):
        print('B')

class C(A, B):
    pass

c = C()
c.hi()