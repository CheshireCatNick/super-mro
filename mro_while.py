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


# merge([[E, B, C, A], [F, B, D, A], [G, C, D, A], [E, F, G]])
def merge(mro_lists):
    result = []
    while any(mro_lists):
        tail = [cls for _, *tail in mro_lists for cls in tail]
        for candidate, *_ in mro_lists:
            if candidate not in tail:
                result.append(candidate)
                # remove head
                mro_lists = [tail if head is candidate else [head] + tail for head, *tail in mro_lists]
                mro_lists = [mro_list for mro_list in mro_lists if mro_list]
                break
    return result


def mro(cls):
    if cls is object:
        return [object]
    return [cls] + merge([mro(base) for base in cls.__bases__] + [list(cls.__bases__)])

print(mro(H))
print(H.mro())