from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[92]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and all((isprime(int(str(num)[:i + 1])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)