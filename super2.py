class A:
    def hello(self):
        print('hello in A')

class B(A):
    def hello(self):
        print('hello in B')
        super().hello()

class C(A):
    def hello(self):
        print('hello in C')
        #super().hello()

class D(B, C):
    def hello(self):
        print('hello in D')
        super().hello()


b = B()
b.hello()

# d = D()
# d.hello()

#print(D.mro())