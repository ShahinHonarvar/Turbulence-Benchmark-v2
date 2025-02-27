from sympy import primerange, isprime

def all_primes_below_x(x):
    return list(primerange(2, x))

def is_left_truncatable(n, prime_list):
    n_str_list = list(str(n))
    while n_str_list:
        if not isprime(int(''.join(n_str_list))):
            return False
        n_str_list.pop(0)
    return True

def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[88]
    primes = all_primes_below_x(x)
    return sorted([prime for prime in primes if is_left_truncatable(prime, primes)], reverse=True)