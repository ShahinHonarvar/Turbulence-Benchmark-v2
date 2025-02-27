def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_and_right_truncatable(n, is_prime_func):
    if not is_prime_func(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime_func(int(str_n[i:])) or not is_prime_func(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(positive_integers):
    x = positive_integers[86]
    result = [i for i in range(2, x + 1) if left_and_right_truncatable(i, is_prime)]
    return sorted(result, reverse=True)