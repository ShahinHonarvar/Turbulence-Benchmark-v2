def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    truncatable_primes = []

    def is_truncatable(n, truncs=()):
        if not n or n == 1:
            return True
        if n < 0 or any((digit == '0' for digit in str(n))):
            return False
        if not is_prime(n):
            return False
        new_truncs = truncs + (n,)
        return all_left_right_truncatable_prime(n // 10, new_truncs) and is_truncatable(n // 10, new_truncs)
    for prime in (p for p in range(2, x + 1) if is_prime(p)):
        if is_truncatable(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)