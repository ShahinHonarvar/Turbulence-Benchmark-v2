def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, check_func, digits):
    while digits:
        if not check_func(n):
            return False
        n //= 10
        digits -= 1
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    return sorted([n for n in range(7, x) if n > 2 and is_left_truncatable_prime(n, is_prime, len(str(n)))])