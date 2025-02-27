def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_left_right(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_primes(numbers_tuple):
    x = numbers_tuple[69]
    return sorted([n for n in range(2, x + 1) if is_truncatable_left_right(n)], reverse=True)