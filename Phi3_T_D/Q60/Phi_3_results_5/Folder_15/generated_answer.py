def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[6]
    result = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return result[::-1]