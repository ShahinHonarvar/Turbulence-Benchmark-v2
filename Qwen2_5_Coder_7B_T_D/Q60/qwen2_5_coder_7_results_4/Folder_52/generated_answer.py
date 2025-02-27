def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num = n
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[1:])
    num = n
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[:-1])
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)