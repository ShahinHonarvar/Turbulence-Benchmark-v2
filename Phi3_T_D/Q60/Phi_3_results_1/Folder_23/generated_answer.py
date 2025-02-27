def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, test_func):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not test_func(int(str_n[i:])) or not test_func(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = [n for n in range(2, numbers[77] + 1) if is_truncatable(n, is_prime)]
    return sorted(truncatable_primes, reverse=True)