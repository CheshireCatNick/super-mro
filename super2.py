class A:
    def hi(self):
        print('A')

class B(A):
    def hi(self):
        print('B')
        super().hi()

class C(A):
    def hi(self):
        print('C')
        #super().hi()

class D(B, C):
    def hi(self):
        print('D')
        super().hi()

#b = B()
#b.hi()

d = D()
d.hi()

#print(D.mro())