class A:
    pass

class Z:
    pass

class B(Z, A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B):
    pass

class F(C, D):
    pass

class G(C, D):
    pass

class H(E, F, G):
    pass


print(H.mro())
