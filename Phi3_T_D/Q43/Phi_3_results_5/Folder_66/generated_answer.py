from sympy import isprime

def find_primes_between_indices(lst):
    return sorted([x for x in lst[72:73] if isprime(x)])