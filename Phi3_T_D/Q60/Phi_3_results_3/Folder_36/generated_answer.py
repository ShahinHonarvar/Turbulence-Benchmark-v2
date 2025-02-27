def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    if n not in primes:
        return False
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i or None])) for i in range(1, len(str_n))))

def all_left_right_truncatable_primes(numbers):
    x = numbers[992]
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    return sorted([p for p in primes if is_truncatable_prime(p, primes)])