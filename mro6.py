class A: 
    def hello(self):
        print('A')

class B:
    def hello(self):
        print('B')

class C:
    def hello(self):
        print('C')

class D(A, B):
    def hello(self):
        # directly using super() will fail since __class__ will be the original D in class namespace
        # https://docs.python.org/3/reference/datamodel.html#creating-the-class-object
        super(self.__class__, self).hello()


print(D.mro())
d = D()
d.hello()

D = type('D', (B, A), dict(D.__dict__))
print(D.mro())
d = D()
d.hello()

# no longer supported in python3
D.__bases__ = (C, B, A)
print(D.mro())
d = D()
d.hello()
