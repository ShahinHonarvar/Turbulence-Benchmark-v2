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

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if str(n)[1:] else 0
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = [n for n in range(2, x) if is_prime(n) and '0' not in str(n)]
    left_truncatable_primes = [n for n in primes if is_left_truncatable(n)]
    return sorted(left_truncatable_primes, reverse=True)