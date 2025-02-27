def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, is_prime_func):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime_func(int(str_n[i:])) or not is_prime_func(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    prime_list = [i for i in range(2, x + 1) if is_truncatable(i, is_prime)]
    return sorted(prime_list, reverse=True)