from sympy import isprime, primerange

def is_truncatable_prime(n, primes):
    str_n = str(n)
    return all((isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n) - i])) for i in range(len(str_n))))

def all_left_right_truncatable_prime(t):
    x = t[975]
    primes = list(primerange(11, x + 1))
    return sorted([p for p in primes if is_truncatable_prime(p, primes)], reverse=True)