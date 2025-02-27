def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    ns = str(n)
    return all((is_prime(int(ns[i:])) and is_prime(int(ns[:-i or None])) for i in range(1, len(ns))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[428]
    if x < 11:
        return []
    primes = [n for n in range(2, x + 1) if is_prmime(n) and is_truncatable_prime(n)]
    return sorted(primes, reverse=True)