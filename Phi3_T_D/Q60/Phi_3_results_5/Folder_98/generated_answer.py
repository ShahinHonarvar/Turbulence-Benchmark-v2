def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_for_all_truncations(n, base=10):
    if not is_prime(n):
        return False
    num_str = str(n)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    if x < 11:
        return []
    truncatable_primes = [p for p in range(11, x + 1) if is_prime_for_all_truncations(p)]
    return sorted(truncatable_primes, reverse=True)