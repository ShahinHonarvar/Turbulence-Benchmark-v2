import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, sieve, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or str_n[i:] not in sieve:
            return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:i + 1])):
            return False
    return True

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return {num for num, is_prime in enumerate(sieve) if is_prime}

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    sieve = sieve_of_eratosthenes(x)
    primes = [p for p in sieve if p < 10 or p > 20]
    return sorted([p for p in sieve if is_truncatable_prime(p, sieve, primes)])