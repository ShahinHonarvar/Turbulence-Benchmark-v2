def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if not is_prime(num):
        return False
    if num < 10:
        return True
    return is_left_truncatable_prime(int(str(num)[1:]))

def all_left_truncatable_prime(data):
    x = data[28]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)