class A:
    pass

class B:
    pass

class C(A, B):
    pass


print(C.__bases__)
print(C.mro())
