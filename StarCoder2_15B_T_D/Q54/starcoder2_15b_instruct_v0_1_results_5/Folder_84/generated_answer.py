def is_right_truncatable(n):
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    return is_right_truncatable(n // 10)

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for n in numbers:
        if n > 0 and is_prime(n) and is_right_truncatable(n):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)