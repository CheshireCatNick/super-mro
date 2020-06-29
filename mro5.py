class A:
    pass

class B(A):
    pass

class C(A, B):
    pass


print(C.mro())