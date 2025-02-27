def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n, primes_set):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = []
    for prime in range(2, x):
        if is_left_truncatable_prime(prime) and is_right_truncatable_prime(prime, primes_set):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)