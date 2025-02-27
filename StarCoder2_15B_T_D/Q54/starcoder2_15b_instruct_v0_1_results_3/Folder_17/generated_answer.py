import math

def all_right_truncatable_prime(t):
    x = t[36]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        temp = prime
        while temp > 9:
            temp = int(str(temp)[:-1])
            if not is_prime(temp):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True