def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    tmp = n
    while tmp > 0:
        if not is_prime(tmp):
            return False
        tmp = tmp % 10 ** (len(str(n)) - 1)
        n = n // 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)