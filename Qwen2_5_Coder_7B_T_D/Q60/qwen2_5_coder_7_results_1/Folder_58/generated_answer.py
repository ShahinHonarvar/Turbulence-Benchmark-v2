from sympy import isprime, primerange

def all_left_right_truncatable_prime(tup):
    x = tup[975]
    primes = list(primerange(2, x + 1))
    left_right_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_truncatable = True
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])) or not isprime(int(str_prime[:-i - 1])):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable.append(prime)
    return sorted(left_right_truncatable, reverse=True)