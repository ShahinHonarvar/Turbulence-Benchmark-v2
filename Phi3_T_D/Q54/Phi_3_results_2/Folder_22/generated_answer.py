def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    if n < 10 or n not in primes_set:
        return False
    while n > 0:
        if n not in primes_set:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    global right_truncatable_primes
    x = numbers[85]
    right_truncatable_primes = []
    for prime in range(2, x):
        if is_prime(prime):
            right_truncatable_primes.append(prime)
    right_truncatable_primes = sorted(set(filter(lambda prime: is_right_truncatable_prime(prime, right_truncatable_primes), right_truncatable_primes)))
    return right_truncatable_primes