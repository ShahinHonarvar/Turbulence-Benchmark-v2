from sympy import isprime

def is_left_truncatable(n, prime_set):
    str_n = str(n)
    while len(str_n) > 0:
        if not isprime(n) or n not in prime_set:
            return False
        str_n = str_n[1:]
        n = int(str_n)
    return True

def all_left_truncatable_prime(numbers):
    primes = {x for x in range(2, numbers[79]) if isprime(x) and '0' not in str(x)}
    result = [p for p in primes if is_left_truncatable(p, primes)]
    return sorted(result, reverse=True)