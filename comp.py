def union(A,B):
    return [x for x in A] + [y for y in B if y not in A]

def intsect(A,B):
    return union([x for x in A if x in B],[y for y in B if y in A])

def diff(U,A):
    return [x for x in U if not x in A]

def symm_diff(A,B):
    return union([x for x in A if x not in B],[y for y in B if y not in A])

def cart_prod(A,B):
    return [(x,y) for x in A for y in B]