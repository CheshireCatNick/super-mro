class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, C):
    pass

class F(B, D):
    pass

class G(C, D):
    pass

class H(E, F, G):
    pass


print(H.mro())