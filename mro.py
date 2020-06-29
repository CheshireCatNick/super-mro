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


# merge([E, B, C, A], [F, B, D, A], [G, C, D, A], [E, F, G])
def merge(mro_lists):
    if not any(mro_lists):
        return []
    mro_lists = list(filter(lambda mro: len(mro) > 0, mro_lists))
    tail_classes = [cls for _, *tail in mro_lists for cls in tail]
    for candidate, *_ in mro_lists:
        if candidate not in tail_classes:
            mro_lists_without_candidate = [tail if head is candidate else [head, *tail] for head, *tail in mro_lists]
            return [candidate] + merge(mro_lists_without_candidate)
    raise Exception('no legal mro')

def mro(cls):
    if cls is object:
        return [object]
    return [cls] + merge([mro(base) for base in cls.__bases__] + [list(cls.__bases__)])

print(mro(H))
print(H.mro())