def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    primes = [n for n in range(2, x) if is_prime(n) and '0' not in str(n)]
    truncatable_primes = [n for n in primes if left_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)