def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[:-1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return result