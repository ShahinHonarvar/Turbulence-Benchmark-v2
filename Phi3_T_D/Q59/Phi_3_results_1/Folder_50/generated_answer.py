def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not str(n).startswith('1') or '0' in str(n):
        return False
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp = temp % 10 ** (len(str(temp)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    return sorted([n for n in range(2, x, 2) if is_left_truncatable_prime(n)], reverse=True)