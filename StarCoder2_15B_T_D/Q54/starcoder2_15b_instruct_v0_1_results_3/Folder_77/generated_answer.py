import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(primes):
    x = primes[767]
    right_truncatable_primes = []
    for i in range(len(str(x))):
        if is_prime(int(str(x)[:len(str(x)) - i])):
            right_truncatable_primes.append(int(str(x)[:len(str(x)) - i]))
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes