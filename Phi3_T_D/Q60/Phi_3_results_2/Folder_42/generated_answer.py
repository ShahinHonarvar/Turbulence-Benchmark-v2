import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    all_primes = filter(is_prime, range(2, x + 1))
    left_right_truncatable_primes = [num for num in all_primes if is_left_and_right_truncatable_prime(num)]
    return sorted(left_right_truncatable_primes, reverse=True)