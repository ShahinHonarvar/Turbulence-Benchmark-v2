def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable(n):
    if not is_prime(n):
        return False
    num_str = str(n)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    result = [p for p in range(x, 0, -1) if is_left_right_truncatable(p)]
    return result