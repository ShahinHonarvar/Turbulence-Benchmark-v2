from sympy import isprime

def find_primes_between_indices(int_list):
    primes = [num for num in int_list[33:36] if isprime(num)]
    primes.sort()
    return primes