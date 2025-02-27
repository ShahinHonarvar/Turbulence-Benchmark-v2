def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num >= 10:
        num = int(str(num)[1:])
        if not is_prime(num):
            return False
        num = int(str(num)[:-1])
        if not is_prime(num):
            return False
    return True