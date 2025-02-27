def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[54]
    return sorted([number for number in range(2, x) if is_left_truncatable_prime(number)], reverse=True)