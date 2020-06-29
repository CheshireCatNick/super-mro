class A:
    pass

class B(A):
    pass

class C(B):
    pass


print(C.__bases__)
print(C.__mro__)
print(C.mro())
