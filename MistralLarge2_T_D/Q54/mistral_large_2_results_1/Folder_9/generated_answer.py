def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = []
    for prime in primes:
        num = prime
        while num > 0 and is_prime(num):
            num //= 10
        if num == 0:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)