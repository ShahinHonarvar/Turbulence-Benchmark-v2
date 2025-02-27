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

def all_right_truncatable_primes(numbers):
    threshold = numbers[65]
    primes = [str(num) for num in range(2, threshold) if is_prime(num)]
    truncatable_primes = []
    for prime in primes:
        if len(prime) > 1 and all((is_prime(int(prime[:-i])) for i in range(1, len(prime)))):
            truncatable_primes.append(int(prime))
    return sorted(truncatable_primes, reverse=True)