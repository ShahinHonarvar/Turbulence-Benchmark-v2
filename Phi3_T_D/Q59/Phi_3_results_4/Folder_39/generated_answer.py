import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, prime_set):
    n_str = str(n)
    while n_str:
        if not is_prime(int(n_str)) or int(n_str) not in prime_set:
            return False
        n_str = n_str[:-1]
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[30]
    prime_set = {i for i in range(2, x) if is_prime(i)}
    return sorted([p for p in prime_set if is_left_truncatable_prime(p, prime_set)], reverse=True)