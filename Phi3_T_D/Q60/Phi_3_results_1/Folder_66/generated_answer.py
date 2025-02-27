def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(x):
    str_x = str(x)
    for i in range(1, len(str_x)):
        if not (is_prime(int(str_x[i:])) and is_prime(int(str_x[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True)