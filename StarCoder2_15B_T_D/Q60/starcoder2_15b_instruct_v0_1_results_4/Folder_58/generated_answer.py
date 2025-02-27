def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n):
        return False
    return is_truncatable_prime(n // 10)