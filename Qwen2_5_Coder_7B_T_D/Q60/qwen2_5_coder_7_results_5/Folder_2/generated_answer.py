def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if not is_prime(int(str_n[:i + 1])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[618]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])