def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    while len(n_str) > 1:
        n_str = n_str[1:]
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[:-1]
        if not is_prime(int(n_str)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for n in numbers:
        if is_left_right_truncatable(n):
            result.append(n)
    result.sort(reverse=True)
    return result