from sympy import isprime

def composite_nums_between_indices(lst):
    if len(lst) < 55:
        return set()
    composites = {x for x in lst[50:55] if not isprime(x) and x > 1}
    return composites