def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n_str = str(n)
    while len(n_str) > 1:
        n_str = n_str[1:]
        if not is_prime(int(n_str)):
            return False
    return True

def all_left_truncatable_primes(numbers):
    x = numbers[79]
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes, reverse=True)