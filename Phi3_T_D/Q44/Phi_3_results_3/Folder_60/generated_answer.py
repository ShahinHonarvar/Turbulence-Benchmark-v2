from sympy import isprime

def composite_nums_between_indices(lst):
    return set((x for i, x in enumerate(lst[29:52], start=29) if not isprime(x) and x > 1))