def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n_str = str(n)
    while n_str:
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[:-1]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    return sorted([i for i in range(2, x, 2) if i > 5 and is_left_truncatable_prime(i)], reverse=True)