from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[55]
    left_truncatable_primes = []

    def is_left_truncatable(num, primes):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or int(str_num) not in primes:
                return False
        return True
    prime_sieve = [False, False] + [True] * (x - 1)
    primes = []
    for p in range(2, x):
        if prime_sieve[p]:
            primes.append(p)
            for i in range(p * p, x, p):
                prime_sieve[i] = False
    for prime in reversed(primes):
        if is_left_truncatable(prime, primes):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes