def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n_str = str(n)
    while n > 0:
        if not is_prime(n):
            return False
        n = int(n_str[1:]) if len(n_str) > 1 else 0
        n_str = n_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])