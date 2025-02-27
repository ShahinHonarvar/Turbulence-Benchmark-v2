from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[4]
    primes = set()
    for n in range(2, x):
        str_n = str(n)
        if isprime(n) and all((isprime(int(str_n[i:])) for i in range(len(str_n)))):
            primes.add(n)
    return sorted(list(primes))